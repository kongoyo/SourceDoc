package com.psd.utils;

import com.ibm.as400.access.AS400;
import com.ibm.as400.access.CommandCall;
import com.ibm.as400.access.PrintObjectInputStream;
import com.ibm.as400.access.SpooledFile;

public class Main 
{
    public static void main( String[] args )
    {
        try {
            // Class.forName("com.ibm.as400.access.AS400JDBCDriver");
            // System.out.println("AS400JDBCDriver loaded!");
            String system = "172.16.13.58";
            String usr = "ibmecs";
            String pwd = "ibmecsusr";
            String cmd = "WRKACTJOB OUTPUT(*PRINT)";

            // Login
            AS400 sys = new AS400(system, usr, pwd);
            
            // Execute command
            CommandCall cmdcall = new CommandCall(sys);
            cmdcall.run(cmd);
            
            // Retrieve Job
            System.out.println(cmdcall.getServerJob());

            // Retrieve Job Splf 
            SpooledFile splf = new SpooledFile(sys, system, 0, pwd, usr, cmd);
            System.out.println(splf);
            String splfjob = splf.getJobName();
            PrintObjectInputStream splfinp = splf.getInputStream();
            // SpooledFileViewer splf = new SpooledFileViewer(splfout);
            System.out.println(splfinp);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
