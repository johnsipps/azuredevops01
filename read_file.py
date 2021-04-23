from azure.storage.blob import BlockBlobService
import pandas as pd
import tables

STORAGEACCOUNTNAME= jdlstoregen2
STORAGEACCOUNTKEY= 'G9G3BNiX10/vjfDJy9PeJUpCRz5kAdA8gJKE5kJq72+quE7cP4fbDduHNjrh4i8rxK+siHDarQyUYyn9X8f0Uw=='
LOCALFILENAME= NYCTripSmall.parquet
CONTAINERNAME= input
BLOBNAME= NYCTripSmall.parquet

#download from blob
t1=time.time()
blob_service=BlockBlobService(account_name=STORAGEACCOUNTNAME,account_key=STORAGEACCOUNTKEY)
blob_service.get_blob_to_path(CONTAINERNAME,BLOBNAME,LOCALFILENAME)
t2=time.time()
print(("It takes %s seconds to download "+BLOBNAME) % (t2 - t1))