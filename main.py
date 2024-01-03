from utils.db_connector import DbConnector
from models.visit_sub_type import VisitSubType
from scripts.acuity_appointment_type_import import AcuityImporter
dbConProd = DbConnector(host='wos-production3.cc5m4dlh7oxc.us-east-1.rds.amazonaws.com',
                    user='WOSADMIN', password='HorseBarnes1!', schema='celia')

acuityImporter = AcuityImporter()

def get_visit_sub_type_info() -> set[VisitSubType]:
    query = 'select visitSubTypeId, abbreviation, name, minimumBillableTime from visitSubTypes;'
    dbConProd.cursor.execute(query)
    visitSubTypes = set([VisitSubType(result[0], result[1], result[2], result[3]) for result in dbConProd.cursor.fetchall()])
    return visitSubTypes

if __name__ == '__main__':
    visit_subtypes = get_visit_sub_type_info()
    acuityImporter.login('pstevenson@wellbox.care', 'Wellbox123!$')
    acuityImporter.input_appointment_types(visit_subtypes)