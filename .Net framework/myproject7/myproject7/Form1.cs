using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using com.ibm.as400.access;

namespace myproject7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void radButton1_Click(object sender, EventArgs e)
        {
            try
            {
                radLabel1.Text = "Somebody click the button!!!";
                AS400 as400 = new AS400("pub400.com", "clhsteve", "Tp6xu4vm0sir");
            } catch (Exception ex) {
                Console.Out.Write(ex.Message);
            }
        }
            
    }
}
