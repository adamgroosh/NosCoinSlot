from boa.interop.Neo.Blockchain import GetBlock
from boa.interop.Neo.Block import *
from boa.interop.Neo.Runtime import CheckWitness, Serialize, Deserialize, Log
from boa.interop.Neo.Storage import GetContext, Put

# Main Operation
#
def Main(operation, args):

    if len(args) != 1:
        Log("ERROR: Incorrect number of arguments")
        return False

    salt = args[0]

    # Act based on requested operation
    if operation == "GenerateRandom":
        height = GetHeight()
        header = GetHeader(height)
        consensus = header.ConsensusData >> 32
        random = (consensus * salt) >> 32
        if random < 100 and random > 10:
            random = random * random
        elif random < 10:
            random = random * random * consensus

        Put(GetContext(), "random", random)
            
    else:
        Log("[!] Operation not found!")

    return False

