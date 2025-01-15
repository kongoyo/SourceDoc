package com.psd.utils;

import com.ibm.as400.access.AS400;
import com.ibm.as400.access.CommandCall;

public class Main 
{
    public static void main( String[] args )
    {
        try {
            Class.forName("com.ibm.as400.access.AS400JDBCDriver");
            System.out.println("AS400JDBCDriver loaded!");
            String system = "172.16.13.58";
            String usr = "ibmecs";
            String pwd = "ibmecsusr";
            String cmd = "WRKACTJOB";
            AS400 sys = new AS400(system, usr, pwd);
            CommandCall cmdcall = new CommandCall(sys);
            cmdcall.run(cmd);
            System.out.println(cmdcall.getClass());
        } catch (Exception e) {
            System.out.println("JDBC Driver Not Found!");
        }
    }
}
