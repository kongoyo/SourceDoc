using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Text.RegularExpressions;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using com.ibm.as400.access;

namespace myproject8
{
    public partial class Form1 : Form
    {
        private readonly string _profilesFilePath = Path.Combine(Application.LocalUserAppDataPath, "profiles.json");

        public Form1()
        {
            InitializeComponent();
            LoadProfilesIntoComboBox();
        }

        private void LoadProfilesIntoComboBox()
        {
            var selectedItem = profileComboBox.SelectedItem;
            profileComboBox.Items.Clear();
            profileComboBox.Items.Add("手動輸入"); // Add a default option for manual entry

            if (File.Exists(_profilesFilePath))
            {
                try
                {
                    var json = File.ReadAllText(_profilesFilePath);
                    var profiles = JsonSerializer.Deserialize<List<ConnectionProfile>>(json);
                    if (profiles != null)
                    {
                        profiles.ForEach(p => profileComboBox.Items.Add(p));
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"讀取設定檔時發生錯誤: {ex.Message}", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }

            if (selectedItem != null && profileComboBox.Items.Contains(selectedItem))
                profileComboBox.SelectedItem = selectedItem;
            else
                profileComboBox.SelectedIndex = 0;
        }

        private async void button1_Click(object sender, EventArgs e)
        {
            string conn_sysip = systemip.Text;  // Get System IP Address
            string conn_userid = userid.Text;   // Get System User ID
            char[] conn_userpw = userpw.Text.ToCharArray();  // Get System User Password

            // --- 1. Input Validation (No try-catch needed) ---
            // validate connect System IP
            string pattern = @"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b";
            if (!Regex.IsMatch(conn_sysip, pattern))
            {
                cmdstr.Text = "IP addr is not correct.";
                return;
            }

            // validate connect System User ID
            if (conn_userid.Length == 0 || conn_userid.Length > 10) // IBM i User IDs are typically 1-10 chars
            {
                cmdstr.Text = "User Id length is not correct.";
                return;
            }

            // --- 2. Asynchronous Connection and Command Execution ---
            button1.Enabled = false;
            cmdstr.Text = "Connecting...";
            textBox1.Clear();

            AS400 as400 = null;
            try
            {
                // Run the long-running operation on a background thread
                await Task.Run(() =>
                {
                    try
                    {
                        as400 = new AS400(conn_sysip, conn_userid, conn_userpw);
                        // Setting a timeout is good practice
                        // as400.setConnectionTimeout(15000); // 15 seconds

                        // 設定 Coded Character Set ID (CCSID) 以匹配 IBM i 系統。
                        // 繁體中文環境通常使用 937。請與您的系統管理員確認正確的 CCSID。
                        as400.setCcsid(937);

                        CommandCall cmd = new CommandCall(as400);

                        // Run the command.
                        if (cmd.run("CRTLIB TBXSAMPLE"))
                        {
                            this.Invoke((MethodInvoker)delegate {
                                cmdstr.Text = cmd.getCommand() + " executed successfully.";
                            });
                        }
                        else
                        {
                            this.Invoke((MethodInvoker)delegate {
                                cmdstr.Text = "Command failed";
                            });
                        }

                        // If messages were produced from the command, print them
                        var messagelist = cmd.getMessageList();
                        if (messagelist.Length > 0)
                        {
                            var messageBuilder = new StringBuilder();
                            foreach (var message in messagelist)
                            {
                                messageBuilder.AppendLine($"{message.getID()}: {message.getText()}");
                            }
                            this.Invoke((MethodInvoker)delegate {
                                textBox1.Text = messageBuilder.ToString();
                            });
                        }
                    }
                    finally
                    {
                        // --- 3. Guaranteed Resource Cleanup ---
                        as400.disconnectAllServices();
                    }
                });
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            finally
            {
                button1.Enabled = true;
                if (!cmdstr.Text.EndsWith("...")) // Don't clear if it's still showing "Connecting..."
                {
                    // Optionally clear fields after operation
                    // systemip.Clear();
                    // userid.Clear();
                    // userpw.Clear();
                }
            }
        }

        private void closeButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void manageProfilesButton_Click(object sender, EventArgs e)
        {
            using (var profileForm = new ProfileManagerForm())
            {
                // Show the form. After it's closed, reload profiles in case of changes.
                profileForm.ShowDialog();
                LoadProfilesIntoComboBox();
            }
        }

        private void profileComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (profileComboBox.SelectedItem is ConnectionProfile selectedProfile)
            {
                // Populate fields from the selected profile
                systemip.Text = selectedProfile.SystemIP;
                userid.Text = selectedProfile.UserId;
                userpw.Text = selectedProfile.Password;
                systemip.Enabled = false;
                userid.Enabled = false;
                userpw.Enabled = false;
            }
            else // This handles the "手動輸入" case
            {
                systemip.Clear();
                userid.Clear();
                userpw.Clear();
                systemip.Enabled = true;
                userid.Enabled = true;
                userpw.Enabled = true;
            }
        }
    }
}
