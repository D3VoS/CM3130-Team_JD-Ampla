USE master
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'AMPLA_DATABASE')
	DROP DATABASE AMPLA_DATABASE

CREATE DATABASE AMPLA_DATABASE

USE AMPLA_DATABASE
GO

IF OBJECT_ID ('Account','U') IS NOT NULL
	DROP TABLE Account

CREATE TABLE Account(
	accountID		NCHAR(10)		NOT NULL,
	firstName		NVARCHAR(30)	NOT NULL,
	lastName		NVARCHAR(30)	NOT NULL,
	title			NVARCHAR(10)	NOT NULL,
	dob				DATE			NOT NULL,
	country			NVARCHAR(30)	NOT NULL,
	emailAddress	NVARCHAR(50)	NOT NULL,
	password		NVARCHAR(30)	NOT NULL,

	isAdmin			BIT				NOT NULL,
	isAthlete		BIT				NOT NULL,
	
	CONSTRAINT pk_account PRIMARY KEY (accountID),
	CONSTRAINT ck_customer_id CHECK (accountID LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
	CONSTRAINT ck_title CHECK (title IN ('Mr', 'Mrs', 'Ms', 'Sir', 'Dame'))
)
GO

IF OBJECT_ID ('Event','U') IS NOT NULL
	DROP TABLE Event

CREATE TABLE Event(
	eventID			NCHAR(10)		NOT NULL,
	eventName		NVARCHAR(30)	NOT NULL,
	creator			NCHAR(10)		NOT NULL,
	dateTime		DATETIME		NOT NULL,
	location		NTEXT			NOT NULL,
	duration		INT				NOT NULL,
	description		NTEXT			NOT NULL,
	capacity		INT				NOT NULL,
	cost			SMALLMONEY		NOT NULL,
	booked			INT				NOT NULL,
	
	CONSTRAINT pk_event PRIMARY KEY (eventID),
	CONSTRAINT fk_event_account FOREIGN KEY (creator) REFERENCES Account (accountID)
		ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT ck_event_id CHECK (eventID LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
	CONSTRAINT ck_max_cap CHECK (booked <= capacity)
)
GO

IF OBJECT_ID ('Booking','U') IS NOT NULL
	DROP TABLE Booking

CREATE TABLE EventBooking(
	bookingID		NCHAR(10)		NOT NULL,
	eventID			NCHAR(10)		NOT NULL,
	accountID		NCHAR(10)		NOT NULL,

	CONSTRAINT pk_booking PRIMARY KEY (bookingID),
	CONSTRAINT fk_eb_event FOREIGN KEY (eventID) REFERENCES Event (eventID),
	CONSTRAINT fk_eb_account FOREIGN KEY (accountID) REFERENCES Account (accountID),
	CONSTRAINT ck_booking_id CHECK (bookingID LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
GO

