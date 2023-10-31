PRAGMA foreign_keys = ON;

INSERT INTO licenseType
VALUES
    (1, "Copyleft","When software is in the public domain, anyone can modify and use the software without any restrictions."),
    (2, "PublicDomain","They contain minimal requirements about how the software can be modified or redistributed. This type of software license is perhaps the most popular license used with free and open source software."),
    (3, "Copyright", "A public license or public copyright licenses is a license by which a copyright holder as licensor can grant additional copyright permissions to any and all persons in the general public as licensees."),
    (4, "LGPL", "It allows you to link to open source libraries in your software. If you simply compile or link an LGPL-licensed library with your own code, you can release your application under any license you want, even a proprietary license.");

INSERT INTO Machine
VALUES
    (1, "Library", "Available"),
    (2, "AdmissionOffice","Available"),
    (3, "FinancialAidOffice","Available"),
    (4, "PhysicsLab","Available"),
    (5, "CSCLab","Retired"),
    (6, "BiologyLab","Retired");

INSERT INTO Software
VALUES
    (1, "Photoshop", "3", "2012-06-02 12:45:30", "2018-06-02 16:40:20","$35","multiple installs","avaliable"),
    (2, "Microsoft Word", "2","2019-08-10 14:30:15","2025-06-02 16:40:20","$100","per active copy","avaliable"),
    (3, "Google Chrome", "1","2020-03-11 13:23:11","2025-06-02 16:40:20","$150", "5years","avaliable"),
    (4, "Skype", "4", "2021-03-01 11:50:30", "2024-06-02 16:40:20","$200","multiple installs","unavaliable");

INSERT INTO MachineSoftware
VALUES
    (1,1, "2012-06-02 12:45:30","2013-06-02 12:45:30" ),
    (1,2, "2019-08-10 14:30:15", NULL),
    (1,3, "2020-03-11 13:23:11", NULL),
    (4,3, "2020-03-11 13:23:11", NULL),
    (4,2, "2019-08-10 14:30:15", NULL);

INSERT INTO Access
VALUES
    (1,"Instructor Access"),
    (2,"Adminstrative Access"),
    (3,"IT Access"),
    (4,"Software Manager Access");

INSERT INTO User
VALUES
    (1, "jComes", "jComes@grandfieldcollege.edu", "1234"),
    (2, "dRosoff", "dRosoff@grandfieldcollege.edu", "feufhwur"),
    (3, "lDanielson", "lDanielson@grandfieldcollege.edu", "dfjie"),
    (4, "mNull", "mNull@grandfieldcollege.edu", "abdeio3830"),
    (5, "aPrice", "aPrice@grandfieldcollege.edu", "8yitje7"),
    (6, "pBennion", "pBennion@grandfieldcollege.edu","84jofne f");
    
INSERT INTO UserAccess
VALUES
    (1,1),
    (2,1),
    (3,1),
    (4,1),
    (5,3),
    (6,2);


INSERT INTO MachineAccess
VALUES
     (1,1),
    (2,3),
    (3,2),
    (4,4),
    (5,3),
    (6,2);

INSERT INTO SoftwareRequest
VALUES
    (1,"2022-01-01","VLC Media Player","Watch interesting content","Great request","2022-01-07","Approved"),
    (2,"2022-02-01","Discord","To communicate with other members of campus.","This can't be approved cause we have teams.","2022-01-07","Approved"),
    (3,"2022-03-01","GTA Auto 5","To relax when stressed linux skills","This can't be approved because this game is gpu heavy.","2022-03-27","Declined"),
    (4,"2022-03-23","Ubuntu Linux","To teach linux skills","This is an awesome request. We will make sure to provided it asap.","2022-03-30","Approved");


INSERT INTO UserSoftwareRequest
VALUES
    (1, 2),
    (2, 4),
    (6, 3);
    
    
    
    INSERT INTO User
    (username,email,password)
VALUES
    ("aBruh", "aBruh@grandfieldcollege.edu", "1234");