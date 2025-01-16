package com.psd.utils;

import com.ibm.as400.access.AS400;
import com.ibm.as400.access.AS400Message;
import com.ibm.as400.access.CommandCall;

public class Main 
{
    public static void main( String[] args )
    {
        try {
            // Create AS400 object to login sys1 & sys2
            AS400 sys1 = new AS400("172.16.13.58", "ibmecs", "ibmecsusr");
            AS400 sys2 = new AS400("172.16.13.57", "ibmecs", "ibmecsusr");

            // Java data to system layout
            // AS400BidiTransform abt = new AS400BidiTransform(937);
            // String dst = abt.toAS400Layout("DBCS中文字");
            // System.out.println(dst);

            // Command類別
            CommandCall cmd = new CommandCall(sys1);
            cmd.run("WRKACTJOB OUTPUT(*PRINT)");
            System.out.println(cmd.getServerJob());
            System.out.println(cmd.getServerJob().getJobLog());
            AS400Message[] msgList = cmd.getMessageList();
            System.out.println(msgList[0]);
            sys1.disconnectService(AS400.COMMAND);

            // Print sys1 command result
            // sys1.connectService(AS400.COMMAND);
            // System.out.println(sys1.isConnected());

            // Print sys2 command result
            // sys2.connectService(AS400.COMMAND);
            // System.out.println(sys1.isConnected());

            // End process
            System.exit(0);

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
