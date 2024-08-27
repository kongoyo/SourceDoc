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
            label2 = new System.Windows.Forms.Label();
            textBox1 = new System.Windows.Forms.TextBox();
            textBox2 = new System.Windows.Forms.TextBox();
            textBox3 = new System.Windows.Forms.TextBox();
            label3 = new System.Windows.Forms.Label();
            textBox4 = new System.Windows.Forms.TextBox();
            label4 = new System.Windows.Forms.Label();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new System.Drawing.Point(527, 28);
            button1.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
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
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new System.Drawing.Point(81, 135);
            label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            label2.Name = "label2";
            label2.Size = new System.Drawing.Size(115, 15);
            label2.TabIndex = 2;
            label2.Text = "cmd messages~!!!!";
            // 
            // textBox1
            // 
            textBox1.Location = new System.Drawing.Point(81, 174);
            textBox1.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            textBox1.Multiline = true;
            textBox1.Name = "textBox1";
            textBox1.Size = new System.Drawing.Size(239, 88);
            textBox1.TabIndex = 3;
            textBox1.Text = "Output something here....";
            // 
            // textBox2
            // 
            textBox2.Location = new System.Drawing.Point(81, 47);
            textBox2.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            textBox2.MaxLength = 15;
            textBox2.Name = "textBox2";
            textBox2.RightToLeft = System.Windows.Forms.RightToLeft.No;
            textBox2.Size = new System.Drawing.Size(121, 23);
            textBox2.TabIndex = 4;
            // 
            // textBox3
            // 
            textBox3.Location = new System.Drawing.Point(226, 47);
            textBox3.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            textBox3.MaxLength = 15;
            textBox3.Name = "textBox3";
            textBox3.RightToLeft = System.Windows.Forms.RightToLeft.No;
            textBox3.Size = new System.Drawing.Size(121, 23);
            textBox3.TabIndex = 6;
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
            // textBox4
            // 
            textBox4.Location = new System.Drawing.Point(367, 47);
            textBox4.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            textBox4.MaxLength = 15;
            textBox4.Name = "textBox4";
            textBox4.RightToLeft = System.Windows.Forms.RightToLeft.No;
            textBox4.Size = new System.Drawing.Size(121, 23);
            textBox4.TabIndex = 8;
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
            // Form1
            // 
            AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            ClientSize = new System.Drawing.Size(700, 450);
            Controls.Add(textBox4);
            Controls.Add(label4);
            Controls.Add(textBox3);
            Controls.Add(label3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(button1);
            Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            Name = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.Label label4;
    }
}

