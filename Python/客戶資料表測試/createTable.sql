CREATE TABLE ddscinfo.Customer1 (
    cus_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cus_name VARCHAR(100) UNIQUE,
    cus_age INT,
    cus_birth DATE,
    cus_liveAddress VARCHAR(255),
    cus_regAddress VARCHAR(255),
    cus_emailAddress VARCHAR(255),
    cus_bloodType CHAR(3),
    cus_companyName VARCHAR(255)
);
