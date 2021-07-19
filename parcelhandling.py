import logging

# Functions
def show_action(message : str) -> None:
    """ Provide the output for a specific action, in a log file (in folder data_output) and on the console
    input: message describing the action
    """
    logging.debug(message)
    print(f".. {message}")

    return None

def xmlreading(xmldatafile: str) -> list:
    """ Parse an xml-file into a list of directories, with nested directories for recipient and recipient address
    input:  xml file to parse
    output: List of directories (parcels)
    
    We use a list to be able to have duplicate parcel shipment destinations. We place processing actions in a log file.
    Assumption (or limitation): Shipment id and date not further used 
    """

    import xml.etree.ElementTree as ET

    shipping_tree = ET.parse(xmldatafile)
    shipping_root = shipping_tree.getroot()

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S ',
                        filename='./data/output/Log_parserhandling.log',
                        filemode='w')
    show_action(f"Start parsing of shipment")
    shipping_id : str = shipping_root[0].text
    shipping_date : str = shipping_root[1].text
    show_action(f"Handling of shipment with Id {shipping_id} on date {shipping_date}")

    parcel_elements = shipping_root[2]
    parcels : list = []

    for parcel in parcel_elements:

        one_address : dict = {}
        one_address['street'] = parcel[0][1][0].text
        one_address['housenumber'] = parcel[0][1][1].text
        one_address['postalcode'] = parcel[0][1][2].text
        one_address['city'] = parcel[0][1][3].text
    
        one_recipient : dict = {}
        one_recipient['name'] = parcel[0][0].text
        one_recipient['address'] = one_address
        
        one_parcel: dict = {}
        one_parcel['recipient'] = one_recipient
        one_parcel['weight'] = float(parcel[1].text)
        one_parcel['value'] = float(parcel[2].text)
        
        logging.info(
            f"{parcel[0][0].text} {parcel[1].text} {parcel[2].text}  " \
            f"Address: {parcel[0][1][0].text} {parcel[0][1][1].text} {parcel[0][1][2].text} {parcel[0][1][3].text}")

        parcels.append(one_parcel)

    show_action(f"End parsing of shipment")

    return parcels    

# Classes and methods
class Parcel():
    """ Parcel of a shipment 
        Limitation: For recipient and recipient address are not created separate classes
    """

    def __init__(self, parcel_dir) -> None:
        self.recipient_name : str = parcel_dir['recipient']['name']
        self.recipient_address : dir = parcel_dir['recipient']['address']
        self.value : float = parcel_dir['value']
        self.weight : float = parcel_dir['weight']

    def __str__(self) -> str:
        return (f"Recipient {self.recipient_name} with parcel value € {self.value} for {self.weight} kg in {self.recipient_address}")


class Department():
    """  Department which executes an action on parcels """

    def __init__(self, name) -> None:
        self.name : str = name

    def is_handle(self) -> bool:
        """ Part of interface, only implemented in Child classes"""
        pass

    def handling_done(self, name_handling_dept, parcel_parameter_to_check, recipient_name_parcel) -> None:
        """ Part of interface, only implemented in Child classes"""
        pass


class CheckingDepartment(Department):
    """ Department which only checks parcels """

    def __init__(self, name, min_value) -> None:
        Department.__init__(self, name)
        self.min_value: float = min_value

    def is_handle(self, parcel_value=0.0) -> bool:
        """ Check parcel value """
        return (self.min_value <= parcel_value)

    def handling_done(self, name_dept, parcel_value, name_recipient) -> None:
        """ Execute correct checking actions on parcel """
        logging.info(f"Signoff by {name_dept} department for value of EUR {parcel_value} for {name_recipient}")
        print(f"Signoff by {name_dept} department for value of EUR {parcel_value} for {name_recipient}")
        return None


class HandlingDepartment(Department):
    """ Department which handles parcels, i.e. moves parcel further in process """

    def __init__(self, name, min_weight, max_weight) -> None:
        Department.__init__(self, name)
        self.min_weight : float = min_weight
        self.max_weight : float = max_weight

    def is_handle(self, parcel_weight=0.0) -> bool:
        """ Check parcel weight """
        return ( (self.min_weight < parcel_weight) and (parcel_weight <= self.max_weight) )

    def handling_done(self, name_dept, parcel_weight, name_recipient) -> None:
        """ Execute correct handling actions on parcel """
        logging.info(f"{name_dept} department handled parcel of {parcel_weight} kg for {name_recipient}")
        print(f"{name_dept} department handled parcel of {parcel_weight} kg for {name_recipient}")
        return None


def main():
    """ Parse a shipment, process it parcel per parcel and show results 
        Assumption: Parcels are max 1000 kg
    """
    MAX_PARCEL_WEIGHT: float = 1000.0   
    XMLFILE2PARSE = "./data/input/Container_68465468.xml"
    parcel_list = xmlreading(XMLFILE2PARSE)

    mail = HandlingDepartment("Mail", 0.0, 1.0)
    regular = HandlingDepartment("Regular", 1.0, 10.0)
    heavy = HandlingDepartment("Heavy", 10.0, MAX_PARCEL_WEIGHT)
    insurance = CheckingDepartment('Insurance', 1000.0)

    print("")
    show_action(f"Start parcel handling of shipment")
    for input_parcel in parcel_list:
        parcel_to_deliver = Parcel(input_parcel)
        if insurance.is_handle(parcel_to_deliver.value):
            insurance.handling_done(insurance.name, parcel_to_deliver.value, parcel_to_deliver.recipient_name)
        if mail.is_handle(parcel_to_deliver.weight):
            mail.handling_done(mail.name, parcel_to_deliver.weight, parcel_to_deliver.recipient_name)
        elif regular.is_handle(parcel_to_deliver.weight):
            regular.handling_done(regular.name, parcel_to_deliver.weight, parcel_to_deliver.recipient_name)
        elif heavy.is_handle(parcel_to_deliver.weight):
            heavy.handling_done(heavy.name, parcel_to_deliver.weight, parcel_to_deliver.recipient_name)
        else:
            logging.error(f"Parcel {parcel_to_deliver.recipient_name} has invalid weight {parcel_to_deliver.weight}")
            print(f"*** ERROR: Parcel {parcel_to_deliver.recipient_name} has invalid weight {parcel_to_deliver.weight}")
    
    show_action("End parcel handling of shipment")

    return None


if __name__ == "__main__":
    main()
