DROP TABLE IF EXISTS licenseType;
DROP TABLE IF EXISTS Machine;
DROP TABLE IF EXISTS Software;
DROP TABLE IF EXISTS MachineStatus;
DROP TABLE IF EXISTS Access;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS UserAccess;
DROP TABLE IF EXISTS MachineAccess;
DROP TABLE IF EXISTS SoftwareRequest;
DROP TABLE IF EXISTS UserSoftwareRequest;
DROP TABLE IF EXISTS MachineSoftware;

CREATE TABLE licenseType (
  licenseKey INTEGER,
  licenseType TEXT,
  terms TEXT,
  PRIMARY KEY (licenseKey)
);

CREATE TABLE Machine (
  machineKey INTEGER,
  machineName TEXT,
  location TEXT,
  status TEXT,
  PRIMARY KEY (machineKey)
);
CREATE TABLE Software (
  softwareKey INTEGER,
  softwareName TEXT,
  licenseKey INTEGER,
  licenseStartDate TEXT,
  licenseEndDate TEXT,
  price TEXT,
  pricingUnit TEXT,
  availability TEXT,
  PRIMARY KEY (softwareKey), --ON DELETE RESTRICT,
    FOREIGN KEY (licenseKey) REFERENCES licenseType(licenseKey) ON DELETE RESTRICT
);

CREATE TABLE MachineSoftware (
  machineKey INTEGER,
  softwareKey INTEGER,
  dateInstalled TEXT,
  dateUninstalled TEXT DEFAULT NULL,
  PRIMARY KEY (machineKey, softwareKey)
    FOREIGN KEY (machineKey) REFERENCES Machine(machineKey) ON DELETE RESTRICT,
    FOREIGN KEY (softwareKey) REFERENCES Software(softwareKey) ON DELETE RESTRICT
);

-- CREATE TABLE MachineStatus (
--   statusKey INTEGER,
--   machineKey INTEGER,
--   status TEXT,
--   PRIMARY KEY (statusKey),
--     FOREIGN KEY (machineKey) REFERENCES Machine(machineKey) ON DELETE RESTRICT
-- );


CREATE TABLE Access (
  accessKey INTEGER,
  accessType TEXT,
  PRIMARY KEY (accessKey)
);
CREATE TABLE User (
  userKey INTEGER AUTO_INCREMENT,
  userName TEXT,
  --firstName TEXT, -- just added this
  --lastName TEXT, -- just added this
  email TEXT,
  password TEXT,
  PRIMARY KEY (userKey)
);

CREATE TABLE UserAccess (
  userKey INTEGER,
  accessKey INTEGER,
  PRIMARY KEY (userKey, accessKey),
    FOREIGN KEY (userKey) REFERENCES User(userKey) ON DELETE RESTRICT,
    FOREIGN KEY (accessKey) REFERENCES Access(accessKey) ON DELETE SET NULL
);

CREATE TABLE MachineAccess(
  machinekey INTEGER,
  accessKey INTEGER,
  PRIMARY KEY (machinekey, accessKey),
    FOREIGN KEY (machineKey) REFERENCES Machine(machineKey) ON DELETE RESTRICT,
    FOREIGN KEY (accessKey) REFERENCES Access(accessKey) ON DELETE CASCADE 
);

CREATE TABLE SoftwareRequest (
  requestKey INTEGER,
  requestdate TEXT,
  softwareName TEXT,
  reason TEXT,
  response TEXT DEFAULT NULL,
  responseDate TEXT DEFAULT NULL,
  status TEXT DEFAULT NULL,
  PRIMARY KEY (requestKey)
);

CREATE TABLE UserSoftwareRequest (
  userKey INTEGER,
  requestKey INTEGER,
  PRIMARY KEY (userKey, requestKey)
    FOREIGN KEY (userKey) REFERENCES User(userKey) ON DELETE RESTRICT,
    FOREIGN KEY (requestKey) REFERENCES SoftwareRequest(requestKey) ON DELETE RESTRICT
);

CREATE TABLE USER_EMAIL(
  useremail TEXT
)

 