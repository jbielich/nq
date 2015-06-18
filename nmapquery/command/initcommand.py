#from db import nqdata

def execute(dbm):
    sql = """
        drop table if exists nmap;
        create table nmap (
            sid INTEGER PRIMARY KEY AUTOINCREMENT,
            version TEXT,
            xmlversion TEXT,
            args TEXT,
            types TEXT,
            starttime INTEGER,
            startstr TEXT,
            endtime INTEGER,
            endstr TEXT,
            numservices INTEGER,
            tag, TEXT);

        drop table if exists hosts;
        create table hosts (
            sid INTEGER,
            hid INTEGER PRIMARY KEY AUTOINCREMENT,
            ip4 TEXT,
            ip4num INTEGER,
            hostname TEXT,
            status TEXT,
            tcpcount INTEGER,
            udpcount INTEGER,
            mac TEXT,
            vendor TEXT,
            ip6 TEXT,
            distance INTEGER,
            uptime TEXT,
            upstr TEXT); 

        drop table if exists sequencing;
        create table sequencing (
            hid INTEGER,
            tcpclass TEXT,
            tcpindex TEXT,
            tcpvalues TEXT,
            ipclass TEXT,
            ipvalues TEXT,
            tcptclass TEXT,
            tcptvalues TEXT);

        drop table if exists ports;
        create table ports (
            hid INTEGER,
            port INTEGER,
            type TEXT,
            state TEXT,
            name TEXT,
            tunnel TEXT,
            product TEXT,
            version TEXT,
            extra TEXT,
            confidence INTEGER,
            method TEXT,
            proto TEXT,
            owner TEXT,
            rpcnum TEXT,
            fingerprint TEXT); 

        drop table if exists os;
        create table os (
            hid INTEGER,
            name TEXT,
            family TEXT,
            generation TEXT,
            type TEXT,
            vendor TEXT,
            accuracy INTEGER);
    """

    dbm.executescript(sql)
