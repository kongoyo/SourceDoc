using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using com.ibm.as400.access;

namespace myproject8
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string conn_sysip = systemip.Text;  // Get System IP Address
            string conn_userid = userid.Text;   // Get System User ID
            char[] conn_userpw = userpw.Text.ToCharArray();  // Get System User Password

            try
            {
                // validate connect System IP
                string pattern = @"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b";
                if (Regex.IsMatch(conn_sysip, pattern))
                {
                    systemip.Text = conn_sysip;
                }
                else
                {
                    cmdstr.Text = "IP addr is not correct.";
                    return;
                }

                // validate connect System User ID
                if (conn_userid.Length <= 8)
                {
                    userid.Text = conn_userid;
                }
                else
                {
                    cmdstr.Text = "User Id length is not correct.";
                    return;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
                return;
            }

            try
            {
                AS400 as400 = new(conn_sysip, conn_userid, conn_userpw);

                // 設定 Coded Character Set ID (CCSID) 以匹配 IBM i 系統。
                // 繁體中文環境通常使用 937。請與您的系統管理員確認正確的 CCSID。
                as400.setCcsid(937);

                CommandCall cmd = new CommandCall(as400);

                // Run the command.
                if (cmd.run("CRTLIB TBXSAMPLE"))
                {
                    cmdstr.Text = cmd.getCommand() + " executed successfully.";
                }
                else
                {
                    cmdstr.Text = "Command failed";
                }

                // If messages were produced from the command, print them
                var messagelist = cmd.getMessageList();
                
                if (messagelist.Length > 0)
                {
                    cmdstr.Text = "Messages from the command:";
                    var messageBuilder = new StringBuilder();
                    // Use a foreach loop to iterate through all messages
                    foreach (var message in messagelist)
                    {
                        // Append each message's ID and text, followed by a new line.
                        messageBuilder.AppendLine($"{message.getID()}: {message.getText()}");
                    }
                    // Assign the combined string to the TextBox once.
                    textBox1.Text = messageBuilder.ToString();
                }
                // If there are no messages, the TextBox will not be changed.
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            systemip.Clear();
            userid.Clear();
            userpw.Clear();
        }
    }
}
