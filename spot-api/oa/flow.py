import graphene
import datetime
# Local Imports
import resources.configurator as configuration
import resources.impala_engine as impalaEngine
import oa.flow_types as flowTypes


class NetflowQueryType(graphene.ObjectType):
    suspicious = graphene.List(flowTypes.SuspiciousType,
                               date=graphene.Argument(type=graphene.types.String,
                                                      default_value=datetime.date.today(),
                                                      description='A date to use as a reference for suspicious connections. Defaults to today'),
                               ip=graphene.Argument(type=graphene.String,
                                                    default_value=None,
                                                    description='IP of interest'))
    edgeDetails = graphene.String(name=graphene.Argument(graphene.String, default_value="edge"))

    def resolve_suspicious(self, info, **args):
        date = args.get("date")
        ip = args.get("ip")
        limit = args.get("limit")

        db = configuration.db()
        sc_query = ("""
                    SELECT STRAIGHT_JOIN
                        fs.tstart,fs.srcip,fs.dstip,fs.sport,fs.dport,proto,
                        ipkt,ibyt,opkt,obyt,ml_score,rank,srcip_internal,
                        dstip_internal,src_geoloc,dst_geoloc,src_domain,
                        dst_domain,src_rep,dst_rep
                    FROM {0}.flow_scores fs
                    LEFT JOIN {0}.flow_threat_investigation ft
                        ON (( fs.srcip = ft.srcip) OR ( fs.dstip = ft.dstip))
                    WHERE fs.y={1} AND fs.m={2} and fs.d={3}
                        AND ( ft.srcip is NULL AND ft.dstip is NULL )
                    """).format(db, date.year, date.month, date.day)

        sc_filter = ""
        if ip:
            sc_filter = " AND ( fs.srcip='{0}' OR fs.dstip='{0}')".format(ip)

        sc_filter += " ORDER BY rank  limit {0}".format(limit)
        sc_query = sc_query + sc_filter

        return impalaEngine.execute_query_as_list(sc_query)

    def resolve_edgeDetails(self, info, **args):
        db = configuration.db()
        details_query = ("""
                SELECT
                    tstart,srcip,dstip,sport,dport,proto,flags,
                    tos,ibyt,ipkt,input,output,rip,obyt,opkt
                FROM {0}.flow_edge
                WHERE
                    y={1} AND m={2} AND d={3} AND hh={4} AND mn={5}
                    AND ((srcip='{6}' AND dstip='{7}')
                    OR  (srcip='{7}' AND dstip='{6}'))
                ORDER BY tstart
                """).format(db, date.year, date.month, date.day, date.hour, \
                            date.minute, src_ip, dst_ip)

        return impalaEngine.execute_query_as_list(details_query)
