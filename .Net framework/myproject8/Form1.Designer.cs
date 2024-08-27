namespace myproject8
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            button1 = new System.Windows.Forms.Button();
            label1 = new System.Windows.Forms.Label();
            cmdstr = new System.Windows.Forms.Label();
            textBox1 = new System.Windows.Forms.TextBox();
            label3 = new System.Windows.Forms.Label();
            label4 = new System.Windows.Forms.Label();
            systemip = new System.Windows.Forms.MaskedTextBox();
            userid = new System.Windows.Forms.MaskedTextBox();
            userpw = new System.Windows.Forms.MaskedTextBox();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new System.Drawing.Point(527, 28);
            button1.Margin = new System.Windows.Forms.Padding(2);
            button1.Name = "button1";
            button1.Size = new System.Drawing.Size(92, 55);
            button1.TabIndex = 0;
            button1.Text = "Connect";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new System.Drawing.Font("Microsoft JhengHei UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 136);
            label1.Location = new System.Drawing.Point(81, 25);
            label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            label1.Name = "label1";
            label1.Size = new System.Drawing.Size(71, 18);
            label1.TabIndex = 1;
            label1.Text = "System IP";
            label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // cmdstr
            // 
            cmdstr.AutoSize = true;
            cmdstr.Location = new System.Drawing.Point(81, 135);
            cmdstr.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            cmdstr.Name = "cmdstr";
            cmdstr.Size = new System.Drawing.Size(115, 15);
            cmdstr.TabIndex = 2;
            cmdstr.Text = "cmd messages~!!!!";
            // 
            // textBox1
            // 
            textBox1.Location = new System.Drawing.Point(81, 174);
            textBox1.Margin = new System.Windows.Forms.Padding(2);
            textBox1.Multiline = true;
            textBox1.Name = "textBox1";
            textBox1.Size = new System.Drawing.Size(239, 88);
            textBox1.TabIndex = 3;
            textBox1.Text = "Output something here....";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new System.Drawing.Font("Microsoft JhengHei UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 136);
            label3.Location = new System.Drawing.Point(226, 25);
            label3.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            label3.Name = "label3";
            label3.Size = new System.Drawing.Size(56, 18);
            label3.TabIndex = 5;
            label3.Text = "User ID";
            label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new System.Drawing.Font("Microsoft JhengHei UI", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 136);
            label4.Location = new System.Drawing.Point(367, 25);
            label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            label4.Name = "label4";
            label4.Size = new System.Drawing.Size(70, 18);
            label4.TabIndex = 7;
            label4.Text = "Password";
            label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // systemip
            // 
            systemip.Location = new System.Drawing.Point(81, 47);
            systemip.Name = "systemip";
            systemip.Size = new System.Drawing.Size(97, 23);
            systemip.TabIndex = 10;
            systemip.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // userid
            // 
            userid.Location = new System.Drawing.Point(226, 47);
            userid.Name = "userid";
            userid.Size = new System.Drawing.Size(97, 23);
            userid.TabIndex = 11;
            userid.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // userpw
            // 
            userpw.Location = new System.Drawing.Point(367, 47);
            userpw.Name = "userpw";
            userpw.Size = new System.Drawing.Size(97, 23);
            userpw.TabIndex = 12;
            userpw.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // Form1
            // 
            AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            ClientSize = new System.Drawing.Size(700, 450);
            Controls.Add(userpw);
            Controls.Add(userid);
            Controls.Add(systemip);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(textBox1);
            Controls.Add(cmdstr);
            Controls.Add(label1);
            Controls.Add(button1);
            Margin = new System.Windows.Forms.Padding(2);
            Name = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label cmdstr;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.MaskedTextBox systemip;
        private System.Windows.Forms.MaskedTextBox userid;
        private System.Windows.Forms.MaskedTextBox userpw;
    }
}

