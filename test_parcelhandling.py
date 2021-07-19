from parcelhandling import xmlreading, Parcel, HandlingDepartment, CheckingDepartment


# Expected testresults
result_complete_duplicate_shipments: list = [{'recipient': {'address': {'city': 'Bosschenhoofd',
                                                                        'housenumber': '28',
                                                                        'postalcode': '4744AT',
                                                                        'street': 'Marijkestraat'},
                                                            'name': 'Vinny Gankema'},
                                                'value': 0.0,
                                                'weight': 0.02},
               {'recipient': {'address': {'city': 'Rotterdam',
                                          'housenumber': '111',
                                          'postalcode': '3036MN',
                                          'street': 'Meester Willemstraat'},
                              'name': 'Soner Colen'},
                'value': 0.0,
                'weight': 2.0},
               {'recipient': {'address': {'city': 'Wouw',
                                          'housenumber': '115',
                                          'postalcode': '4724BE',
                                          'street': 'Nieuwstraat'},
                              'name': 'Ricardus Proper'},
                'value': 2000.0,
                'weight': 100.0},
               {'recipient': {'address': {'city': 'Zuidhorn',
                                          'housenumber': '97',
                                          'postalcode': '9801BZ',
                                          'street': 'Hoofdstraat'},
                              'name': 'Alvaro ten Cate'},
                'value': 500.0,
                'weight': 11.0},
               {'recipient': {'address': {'city': 'Hilversum',
                                          'housenumber': '43',
                                          'postalcode': '1212BZ',
                                          'street': 'Willem Bontekoestraat'},
                              'name': 'Roland Lubben'},
                'value': 0.0,
                'weight': 3.0},
               {'recipient': {'address': {'city': 'Enschede',
                                          'housenumber': '115',
                                          'postalcode': '7524PB',
                                          'street': 'Overmaat'},
                              'name': 'Ninon Spanjersberg'},
                'value': 1500.0,
                'weight': 10.0},
               {'recipient': {'address': {'city': 'Enschede',
                                          'housenumber': '115',
                                          'postalcode': '7524PB',
                                          'street': 'Overmaat'},
                              'name': 'Ninon Spanjersberg'},
                'value': 1500.0,
                'weight': 10.0},
               {'recipient': {'address': {'city': 'Leusden',
                                          'housenumber': '147',
                                          'postalcode': '3831ZA',
                                          'street': 'Salamander'},
                              'name': 'Montana Martinus'},
                'value': 0.0,
                'weight': 0.7},
               {'recipient': {'address': {'city': 'Zwolle',
                                          'housenumber': '17',
                                          'postalcode': '8024XC',
                                          'street': 'Oleanderlaan'},
                              'name': 'Aisling Kruizenga'},
                'value': 1100.0,
                'weight': 0.9},
               {'recipient': {'address': {'city': 'Nisse',
                                          'housenumber': '1',
                                          'postalcode': '4443RC',
                                          'street': 'Paul Krugerstraat'},
                              'name': 'Bernadet Spijker'},
                'value': 0.0,
                'weight': 4.5},
               {'recipient': {'address': {'city': 'Musselkanaal',
                                          'housenumber': '84',
                                          'postalcode': '9581GD',
                                          'street': 'Schoolstraat'},
                              'name': 'Collin Slaman'},
                'value': 1500.0,
                'weight': 120.0},
               {'recipient': {'address': {'city': 'Waddinxveen',
                                          'housenumber': '176',
                                          'postalcode': '2742TS',
                                          'street': 'Berkengaarde'},
                              'name': 'Collin Slaman'},
                'value': 2000.0,
                'weight': 130.0},
               {'recipient': {'address': {'city': 'Waddinxveen',
                                          'housenumber': '176',
                                          'postalcode': '2742TS',
                                          'street': 'Berkengaarde'},
                              'name': 'Ingetje Hauwert'},
                'value': 0.0,
                'weight': 0.3},
               {'recipient': {'address': {'city': 'Paterswolde',
                                          'housenumber': '68',
                                          'postalcode': '9765CN',
                                          'street': 'Hoofdweg'},
                              'name': 'Amber van der Schaar'},
                'value': 0.0,
                'weight': 1.0},
               {'recipient': {'address': {'city': 'Capelle aan den IJssel',
                                          'housenumber': '30',
                                          'postalcode': '2908BD',
                                          'street': 'Ringspoor'},
                              'name': 'Willemtje Guldemond'},
                'value': 100.0,
                'weight': 15.0},
               {'recipient': {'address': {'city': 'Capelle aan den IJssel',
                                          'housenumber': '30',
                                          'postalcode': '2908BD',
                                          'street': 'Ringspoor'},
                              'name': 'Willemtje Guldemond'},
                'value': 100.0,
                'weight': 15.0},
               {'recipient': {'address': {'city': 'Sint Willebrord',
                                          'housenumber': '125',
                                          'postalcode': '4711KA',
                                          'street': 'Duivenstraat'},
                              'name': 'Zeki Soekhai'},
                'value': 0.0,
                'weight': 0.4}]

result_duplicate_address_different_shipment: list = [{'recipient': {'address': {'city': 'Musselkanaal',
                                                                                'housenumber': '84',
                                                                                'postalcode': '9581GD',
                                                                                'street': 'Schoolstraat'},
                                                                    'name': 'Collin Slaman'},
                                                      'value': 1500.0,
                                                      'weight': 120.0},
                                                     {'recipient': {'address': {'city': 'Waddinxveen',
                                                                                'housenumber': '176',
                                                                                'postalcode': '2742TS',
                                                                                'street': 'Berkengaarde'},
                                                                    'name': 'Collin Slaman'},
                                                      'value': 2000.0,
                                                      'weight': 130.0}]

result_duplicate_address_same_shipment: list = [{'recipient': {'address': {'city': 'Enschede',
                                                                           'housenumber': '115',
                                                                           'postalcode': '7524PB',
                                                                           'street': 'Overmaat'},
                                                               'name': 'Ninon Spanjersberg'},
                                                 'value': 1500.0,
                                                 'weight': 10.0},
                                                {'recipient': {'address': {'city': 'Enschede',
                                                                           'housenumber': '115',
                                                                           'postalcode': '7524PB',
                                                                           'street': 'Overmaat'},
                                                               'name': 'Ninon Spanjersberg'},
                                                 'value': 1500.0,
                                                 'weight': 10.0}]

result_parse_one = [{'recipient': {'address': {'city': 'Bosschenhoofd',
                                               'housenumber': '28',
                                               'postalcode': '4744AT',
                                               'street': 'Marijkestraat'},
                                   'name': 'Vinny Gankema'},
                     'value': 0.0,
                     'weight': 0.02}]

result_parse_empty = []


# Test functions 
#   Tests for parsing of shipment
xml_complete_input = "./data/input/Container_68465468.xml"
def test_parse_complete_duplicate_address():
    assert xmlreading(xml_complete_input) == result_complete_duplicate_shipments

xml_duplicate_address_different_shipment = "./data/input/ContainerTest_duplicate_different_shipment.xml"
def test_parse_duplicate_address_different_shipment():
    assert xmlreading(xml_duplicate_address_different_shipment) == result_duplicate_address_different_shipment

xml_duplicate_address_same_shipment = "./data/input/ContainerTest_duplicate_same_shipment.xml"
def test_parse_duplicate_address_same_shipment():
    assert xmlreading(xml_duplicate_address_same_shipment) == result_duplicate_address_same_shipment

xml_parse_one = "./data/input/ContainerTest_one_shipment.xml"
def test_parse_one_shipment():
    assert xmlreading(xml_parse_one) == result_parse_one

xml_parse_empty = "./data/input/ContainerTest_empty_shipment.xml"
def test_parse_empty_shipment():
    assert xmlreading(xml_parse_empty) == result_parse_empty


#   Tests for processing of parcels in shipment
testparcel_one = {'recipient': {'address': {'city': 'Bosschenhoofd',
                                            'housenumber': '28',
                                            'postalcode': '4744AT',
                                            'street': 'Marijkestraat'},
                                'name': 'Vinny Gankema'},
                  'value': 0.0,
                  'weight': 0.02}

parceltest = Parcel(testparcel_one)
def test_parcel_create():
    " Test parcel creation without address "
    assert (parceltest.recipient_name == 'Vinny Gankema') and (parceltest.value == 0.0) and (parceltest.weight == 0.02)


handle_dept1 = HandlingDepartment("Handle1", 3.0, 7.0)
def test_depthandle_verifyweight():
    " Test if weight is handled correctly by department "
    assert handle_dept1.is_handle(5.0) == True 
    assert handle_dept1.is_handle(8.0) == False
    assert handle_dept1.is_handle(3.0) == False   # Minimum excluded
    assert handle_dept1.is_handle(7.0) == True   # Maximum included

check_dept1 = CheckingDepartment("Check1", 500.0)
def test_deptcheck_verifyvalue():
    " Test if value is checked correctly by department "
    assert check_dept1.is_handle(150.0) == False
    assert check_dept1.is_handle(600.0) == True
    assert check_dept1.is_handle(500.0) == True   # Minimum included
