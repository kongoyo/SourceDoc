SET SCHEMA "DDSCINFO";
DROP TABLE FISHES;
CREATE TABLE FISHES (
                        FISH_NAME FOR COLUMN NAME CHAR(10) NOT NULL DEFAULT,
                        FISH_COLOR FOR COLUMN COLOR CHAR(10) NOT NULL DEFAULT,
                        FISH_WEIGHT FOR COLUMN WEIGHT INT NOT NULL DEFAULT
                );
ALTER TABLE FISHES
        ADD PRIMARY KEY (NAME);
ALTER TABLE FISHES
        ADD CONSTRAINT CST_COLOR CHECK (NAME <> COLOR);

INSERT INTO FISHES
        VALUES
                (
                        'haddock',
                        'white',
                        1
                );
INSERT INTO FISHES
        VALUES
                (
                        'cod',
                        'green',
                        2
                );
INSERT INTO FISHES
        VALUES
                (
                        'hake',
                        'yellow',
                        3
                );
INSERT INTO FISHES
        VALUES
                (
                        'mackerel',
                        'blue',
                        4
                );
INSERT INTO FISHES
        VALUES
                (
                        'tench',
                        'orange',
                        5
                );
INSERT INTO FISHES
        VALUES
                (
                        'sprat',
                        'purple',
                        6
                );
INSERT INTO FISHES
        VALUES
                (
                        'dace',
                        'fuscia',
                        7
                );
INSERT INTO FISHES
        VALUES
                (
                        'rudd',
                        'maroon',
                        8
                );
INSERT INTO FISHES
        VALUES
                (
                        'pike',
                        'plum',
                        9
                );
INSERT INTO FISHES
        VALUES
                (
                        'gudgeon',
                        'lilac',
                        10
                );
INSERT INTO FISHES
        VALUES
                (
                        'white',
                        'white',
                        11
                );
-- violates check constraint CST_COLOR gives error SQL State: 23513
INSERT INTO FISHES
        VALUES
                (
                        'haddock',
                        'magenta',
                        12
                );
-- violates unique constraint gives error SQL State: 23505
SELECT *
        FROM FISHES
        ORDER BY COLOR;;



-- Common table expression
WITH A AS (
             SELECT ROW_NUMBER() OVER (
                            ORDER BY ORDER OF F
                    ) - 1 AS NB,
                    NAME AS NAME
                     FROM FISHES AS F
     ),
     B AS (
             SELECT SMALLINT(NB / 5) + 1 AS OUTROW,
                    SMALLINT(MOD(NB, 5)) + 1 AS OUTCOL,
                    NAME AS NAME
                     FROM A
     ),
     C AS (
             SELECT OUTROW,
                    (
                    CASE
                            WHEN OUTCOL = 1 THEN NAME
                            ELSE NULL
                    END) AS NAME1,
                    (
                    CASE
                            WHEN OUTCOL = 2 THEN NAME
                            ELSE NULL
                    END) AS NAME2,
                    (
                    CASE
                            WHEN OUTCOL = 3 THEN NAME
                            ELSE NULL
                    END) AS NAME3,
                    (
                    CASE
                            WHEN OUTCOL = 4 THEN NAME
                            ELSE NULL
                    END) AS NAME4,
                    (
                    CASE
                            WHEN OUTCOL = 5 THEN NAME
                            ELSE NULL
                    END) AS NAME5
                     FROM B
     )
        SELECT OUTROW,
               MAX(NAME1) COL_1,
               MAX(NAME2) COL_2,
               MAX(NAME3) COL_3,
               MAX(NAME4) COL_4,
               MAX(NAME5) COL_5
                FROM C
                GROUP BY OUTROW
                ORDER BY OUTROW;

/*        