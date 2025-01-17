package com.psd.utils;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

import io.github.mapepire_ibmi.Query;
import io.github.mapepire_ibmi.SqlJob;
import io.github.mapepire_ibmi.types.DaemonServer;
import io.github.mapepire_ibmi.types.QueryResult;

public final class mapepirejapp {
    public static void main(String[] args) throws Exception {
        // Initialize credentials
        DaemonServer creds = new DaemonServer("172.16.13.58", 8076, "ibmecs", "ibmecsusr", false);

        // Establish connection
        SqlJob job = new SqlJob();
        job.connect(creds).get();

        // Initialize and execute query
        Query query = job.query("SELECT * FROM SAMPLE.DEPARTMENT");
        QueryResult<Object> result = query.execute(3).get();

        // Convert to JSON string and output
        ObjectMapper mapper = new ObjectMapper();
        mapper.enable(SerializationFeature.INDENT_OUTPUT);
        String jsonString = mapper.writeValueAsString(result);
        System.out.println(jsonString);
    }
}
