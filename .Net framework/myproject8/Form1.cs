using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
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
            AS400 as400 = new AS400("172.16.14.61", "QSECOFR", "PASSWORD");
            CommandCall cmd = new CommandCall(as400);
            try
            {
                // Run the command.
                if (cmd.run("CRTLIB TBXSAMPLE"))
                    label1.Text = cmd.getCommand();
                else
                    label1.Text = "Command failed";

                // If messages were produced from the command, print them
                AS400Message[] messagelist = cmd.getMessageList();

                if (messagelist.Length > 0)
                {
                    label2.Text = "messages from the command:";
                }

                for (int i = 0; i < messagelist.Length; i++)
                {
                    textBox1.Text = messagelist[i].getID() + ":" + messagelist[i].getText();
                }
            }
            catch (Exception)
            {
            };
        }
    }
}
