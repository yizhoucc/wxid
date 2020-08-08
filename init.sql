
-- create database [IF NOT EXISTS] wx;
-- DEFAULT CHARACTER set utf8 collate utf8_general_ci;
-- use wx;


-- Create the table in the specified schema

CREATE TABLE wx.wxdata
(
    id MEDIUMINT NOT NULL AUTO_INCREMENT primary key,
    wxid varchar(32) NOT NULL, 
    xing varchar(16) NOT NULL,
    app1 varchar(32) NOT NULL,
    id1 varchar(32)  NOT NULL,
    app2 varchar(32),
    id2 varchar(32)  ,
    app3 varchar(32) ,
    id3 varchar(32) 


);
