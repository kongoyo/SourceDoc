//************************
// File: DateExample.java
//************************
 
import java.text.*;
import java.util.*;
import java.util.Date;
 
public class DateExample {
 
   public static void main(String args[]) {
 
     // Get the Date
     Date now = new Date();
 
     // Get date formatters for default, German, and French locales
     DateFormat theDate = DateFormat.getDateInstance(DateFormat.LONG);
     DateFormat germanDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.GERMANY);
     DateFormat frenchDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.FRANCE);
 
     // Format and print the dates
     System.out.println("Date in the default locale: " + theDate.format(now));
     System.out.println("Date in the German locale : " + germanDate.format(now));
     System.out.println("Date in the French locale : " + frenchDate.format(now));  
   } 
}