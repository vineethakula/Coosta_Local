"""
Dumps data from CSV to Parcel DB
"""
import MySQLdb
import csv
import sys
import time

DB_HOST = '54.213.231.130'   #LIVE DB
# DB_HOST = 'localhost'   #LIVE DB
DB_USER = 'coosta_db_user'
DB_USER_PASSWORD = 'coosta_db_pwd'
DB_NAME = 'coosta_db'


def dump_data_in_db(con, data):
    """
    :param data:
    :return:
    """
    con.executemany(
            """INSERT INTO properties_parcel (
            ZIPcode, TaxRateArea_CITY, AIN, RollYear, TaxRateArea,
            AssessorID, PropertyLocation, PropertyType, PropertyUseCode,
            GeneralUseType, SpecificUseType, SpecificUseDetail1,
            SpecificUseDetail2, totBuildingDataLines, YearBuilt,
            EffectiveYearBuilt, SQFTmain, Bedrooms, Bathrooms, Units,
            RecordingDate, LandValue, LandBaseYear, ImprovementValue,
            ImpBaseYear, TotalLandImpValue, HomeownersExemption,
            RealEstateExemption, FixtureValue, FixtureExemption,
            PersonalPropertyValue, PersonalPropertyExemption, isTaxableParcel,
            TotalValue, TotalExemption, netTaxableValue,
            SpecialParcelClassification, AdministrativeRegion, Cluster,
            ParcelBoundaryDescription, HouseNo, HouseFraction,
            StreetDirection, StreetName, UnitNo, City, ZIPcode5, rowID,
            CENTER_LAT, CENTER_LON) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                                            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                            """, data)

if __name__ == '__main__':
    con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_USER_PASSWORD,
                         db=DB_NAME)
    cursor = con.cursor()

    csv_file_path = '/home/deepak/Downloads/Assessor_Parcels_Data_-_2006_thru_20.csv'

    count = 0

    list_of_tuple_to_insert = []

    with open(csv_file_path, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)
        count = 0
        for row in datareader:
            count += 1
            now = time.time()
            # row = [x.strip('$') for x in row]
            row[21] = row[21].strip('$')
            row[23] = row[23].strip('$')
            row[25] = row[25].strip('$')
            row[26] = row[26].strip('$')
            row[27] = row[27].strip('$')
            row[28] = row[28].strip('$')
            row[29] = row[29].strip('$')
            row[30] = row[30].strip('$')
            row[31] = row[31].strip('$')
            row[33] = row[33].strip('$')
            row[34] = row[34].strip('$')
            row[35] = row[35].strip('$')
            list_of_tuple_to_insert.append(tuple(row[:-1]))
            if count == 25000:
                try:
                    dump_data_in_db(cursor, list_of_tuple_to_insert)
                    con.commit()
                    list_of_tuple_to_insert = []
                    count = 0
                    print time.time() - now
                except Exception as exp:
                    print(exp)
                    sys.exit(1)

        try:
            dump_data_in_db(cursor, list_of_tuple_to_insert)
            con.commit()
        except Exception as exp:
            print(exp)
            sys.exit(1)

    print 'done'
    sys.exit(0)