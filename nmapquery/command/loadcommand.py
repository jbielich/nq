import sqlite3
import os
import sys
import time
from libnmap.parser import NmapParser
from db import nqdb
from util import dateutil

def save_report_header(db, rpt):
    loadtime = int(time.time())

    sql = """INSERT INTO
             nmap(loadtime, version, starttime, startstr, endtime, endstr,
             hosts_total, hosts_up, hosts_down,summarystr)
             values(?,?,?,?,?,?,?,?,?,?)"""

    values = (loadtime, rpt.version, int(rpt.started),
              dateutil.unix_to_standard_string((rpt.started)), int(rpt.endtime),
              rpt.endtimestr, int(rpt.hosts_total), int(rpt.hosts_up),
              int(rpt.hosts_down), rpt.summary)

    # Load summary data
    db.execute_with_params(sql, values)

    # Get SID (global key)
    cur = db.query("SELECT sid FROM nmap WHERE loadtime={0}".format(loadtime))
    sid = cur.fetchone()[0]

    return sid

def save_hosts(db, sid, hosts):
    print "saving host information..."

    try:
        sql = """INSERT INTO hosts(sid, ip4, hostname,
        status, mac, vendor, uptime, tcpcount, udpcount)
        values(?,?,?,?,?,?,?,?,?)"""

        for host in hosts:
            ip = host.address
            hostname = host.hostnames[0]  #TODO: set up for multi-hostnames
            status = host.status
            mac = host.mac
            vendor = host.vendor
            uptime = host.uptime
            tcpcount = 0
            udpcount = 0

            for port in host.get_ports():
                if port[1] == 'tcp':
                    tcpcount += 1
                elif port[1] == 'udp':
                    udpcount += 1

            values = (sid, ip, hostname, status, mac, vendor,
                      uptime, tcpcount, udpcount)

            db.execute_with_params(sql, values)

            os_sql = """INSERT INTO os (hid, name, family,
                        generation, type, vendor, accuracy
                        VALUES (?,?,?,?,?,?,?)"""

            for prob in host.os_match_probabilities():
                print prob.name

            #for os in host.os_class_probabilities():
                #values = (hid, os.name, os.osfamily, os.osgen, os.type,
                          #os.vendor, os.accuracy)

    except:
        e = sys.exc_info()
        print e


def execute(db,filename):
    print "Loading %s into database..." % filename 

    rpt = NmapParser.parse_fromfile(filename)
    sid = save_report_header(db,rpt)
    save_hosts(db, sid, rpt.hosts)

    print "File loaded."

