import requests
import time

data_normal = {
    "Retry":{
        "CurrentRank":1.0,
        "PreviousResponseCode":"04",
        "PreviousRetryOptimization":{
            "IsApplicable":"true",
            "Optimizations":{
                "channel":"",
                "removeThreeD":""
            }
        }
    },
    "OriginalTransaction":{
        "RequestCorrelationId":"{{$guid}}",
        "SessionCorrelationId":"0000",
        "TransactionOriginatorId":"18",
        "InternalAmount":58.0,
        "InitialRecurring":"false",
        "AuthDateTime":"2018-11-20T12:21:21Z",
        "TransactionTypeId":"1",
        "Channel":"2",
        "Eci":"4",
        "CurrencyId":"978",
        "EffectiveValues":{
            "AuthorizationType":"0",
            "ChannelType":"2",
            "ChannelSubtype":"1",
            "CredentialOnFileType":"NULL",
            "DwoIndicator":"NULL",
            "WalletProvider":"NULL"
        },
        "Card":{
            "Bin":"451233",
            "ExpiryMonth":11.0,
            "ExpiryYear":2020.0,
            "Cv2ResultType":"3",
            "Cv2Reponse":"U",
            "HolderIp":"NULL",
            "AvsThere":"true",
            "BinDetail":{
                "CardBrand":"1",
                "CardSubtypeId":"1",
                "CardCommercial":"true",
                "CardPrepaid":"true",
                "IssuerCode":"978",
                "IssuerCountryCode":"840",
                "IssuerTypeId":"1"
            },
            "BinInfo":{
                "CardSchemaId":"2",
                "ServiceTypeId":"1",
                "IssuerCode":"400555",
                "CountryCode":"840",
                "ProductCode":"F",
                "ProductSubCode":"",
                "IsCommercial":"false",
                "IsPrivateLabel":"false",
                "BrandCode":"005",
                "IsPrepaid":"false"
            }
        },
        "Merchant":{
            "CountryCode":"840",
            "ProcessorId":"12",
            "CategoryCodeGroup":"7995",
            "MemberId":"12345",
            "Ip":"192.168.0.1"
        }
    }
}
data1 = {
    "Retry":{
        "CurrentRank":1.0,
        "PreviousResponseCode":"04",
        "PreviousRetryOptimization":{
            "IsApplicable":"true",
            "Optimizations":{
                "channel":"",
                "removeThreeD":""
            }
        }
    },
    "OriginalTransaction":{
        "RequestCorrelationId":"{{$guid}}",
        "SessionCorrelationId":"1111",
        "TransactionOriginatorId":"18",
        "InternalAmount":58.0,
        "InitialRecurring":"false",
        "AuthDateTime":"2018-11-20T12:21:21Z",
        "TransactionTypeId":"1",
        "Channel":"2",
        "Eci":"4",
        "CurrencyId":"978",
        "EffectiveValues":{
            "AuthorizationType":"0",
            "ChannelType":"2",
            "ChannelSubtype":"1",
            "CredentialOnFileType":"NULL",
            "DwoIndicator":"NULL",
            "WalletProvider":"NULL"
        },
        "Card":{
            "Bin":"451233",
            "ExpiryMonth":11.0,
            "ExpiryYear":2020.0,
            "Cv2ResultType":"3",
            "Cv2Reponse":"U",
            "HolderIp":"NULL",
            "AvsThere":"true",
            "BinDetail":{
                "CardBrand":"1",
                "CardSubtypeId":"1",
                "CardCommercial":"true",
                "CardPrepaid":"true",
                "IssuerCode":"978",
                "IssuerCountryCode":"840",
                "IssuerTypeId":"1"
            },
            "BinInfo":{
                "CardSchemaId":"2",
                "ServiceTypeId":"1",
                "IssuerCode":"400555",
                "CountryCode":"840",
                "ProductCode":"F",
                "ProductSubCode":"",
                "IsCommercial":"false",
                "IsPrivateLabel":"false",
                "BrandCode":"005",
                "IsPrepaid":"false"
            }
        },
        "Merchant":{
            "CountryCode":"840",
            "ProcessorId":"12",
            "CategoryCodeGroup":"7995",
            "MemberId":"12345",
            "Ip":"192.168.0.1"
        }
    }
}
data2 = {
    "Retry":{
        "CurrentRank":2.0,
        "PreviousResponseCode":"04",
        "PreviousRetryOptimization":{
            "IsApplicable":"true",
            "Optimizations":{
                "channel":"1",
                "removeThreeD":""
            }
        }
    },
    "OriginalTransaction":{
        "RequestCorrelationId":"{{$guid}}",
        "SessionCorrelationId":"1111",
        "TransactionOriginatorId":"18",
        "InternalAmount":58.0,
        "InitialRecurring":"false",
        "AuthDateTime":"2018-11-20T12:21:21Z",
        "TransactionTypeId":"1",
        "Channel":"2",
        "Eci":"4",
        "CurrencyId":"978",
        "EffectiveValues":{
            "AuthorizationType":"0",
            "ChannelType":"2",
            "ChannelSubtype":"1",
            "CredentialOnFileType":"NULL",
            "DwoIndicator":"NULL",
            "WalletProvider":"NULL"
        },
        "Card":{
            "Bin":"451233",
            "ExpiryMonth":11.0,
            "ExpiryYear":2020.0,
            "Cv2ResultType":"3",
            "Cv2Reponse":"U",
            "HolderIp":"NULL",
            "AvsThere":"true",
            "BinDetail":{
                "CardBrand":"1",
                "CardSubtypeId":"1",
                "CardCommercial":"true",
                "CardPrepaid":"true",
                "IssuerCode":"978",
                "IssuerCountryCode":"840",
                "IssuerTypeId":"1"
            },
            "BinInfo":{
                "CardSchemaId":"2",
                "ServiceTypeId":"1",
                "IssuerCode":"400555",
                "CountryCode":"840",
                "ProductCode":"F",
                "ProductSubCode":"",
                "IsCommercial":"false",
                "IsPrivateLabel":"false",
                "BrandCode":"005",
                "IsPrepaid":"false"
            }
        },
        "Merchant":{
            "CountryCode":"840",
            "ProcessorId":"12",
            "CategoryCodeGroup":"7995",
            "MemberId":"12345",
            "Ip":"192.168.0.1"
        }
    }
}
data3 = {
    "Retry":{
        "CurrentRank":3.0,
        "PreviousResponseCode":"04",
        "PreviousRetryOptimization":{
            "IsApplicable":"true",
            "Optimizations":{
                "channel":"1",
                "removeThreeD":""
            }
        }
    },
    "OriginalTransaction":{
        "RequestCorrelationId":"{{$guid}}",
        "SessionCorrelationId":"1111",
        "TransactionOriginatorId":"18",
        "InternalAmount":58.0,
        "InitialRecurring":"false",
        "AuthDateTime":"2018-11-20T12:21:21Z",
        "TransactionTypeId":"1",
        "Channel":"2",
        "Eci":"4",
        "CurrencyId":"978",
        "EffectiveValues":{
            "AuthorizationType":"0",
            "ChannelType":"2",
            "ChannelSubtype":"1",
            "CredentialOnFileType":"NULL",
            "DwoIndicator":"NULL",
            "WalletProvider":"NULL"
        },
        "Card":{
            "Bin":"451233",
            "ExpiryMonth":11.0,
            "ExpiryYear":2020.0,
            "Cv2ResultType":"3",
            "Cv2Reponse":"U",
            "HolderIp":"NULL",
            "AvsThere":"true",
            "BinDetail":{
                "CardBrand":"1",
                "CardSubtypeId":"1",
                "CardCommercial":"true",
                "CardPrepaid":"true",
                "IssuerCode":"978",
                "IssuerCountryCode":"840",
                "IssuerTypeId":"1"
            },
            "BinInfo":{
                "CardSchemaId":"2",
                "ServiceTypeId":"1",
                "IssuerCode":"400555",
                "CountryCode":"840",
                "ProductCode":"F",
                "ProductSubCode":"",
                "IsCommercial":"false",
                "IsPrivateLabel":"false",
                "BrandCode":"005",
                "IsPrepaid":"false"
            }
        },
        "Merchant":{
            "CountryCode":"840",
            "ProcessorId":"12",
            "CategoryCodeGroup":"7995",
            "MemberId":"12345",
            "Ip":"192.168.0.1"
        }
    }
}

ver_list = []

r1 = requests.post("http://localhost:9000", json = data1)
r2 = requests.post("http://localhost:9000", json = data2)
r3 = requests.post("http://localhost:9000", json = data3)

get1 = requests.get("http://localhost:9000/healthz")

#print(get1.text )

#assert correct length
#assert len(get.text.split("|"))==2

if len(get1.text.split("|"))==2:
	ver_list.append(True)
else:
	ver_list.append(False)

print(get1.text)
print("--------------------")

#for i in range(0,4):
#	requests.post("http://localhost:9000", data = data_normal)
#this is ugly, but not sure loop works
rn1 = requests.post("http://localhost:9000", json = data_normal)
rn2 = requests.post("http://localhost:9000", json = data_normal)
rn3 = requests.post("http://localhost:9000", json = data_normal)
rn4 = requests.post("http://localhost:9000", json = data_normal)

get2 = requests.get("http://localhost:9000/healthz")

print(get2.text)
print("--------------------------")

if len(get2.text.split("|"))==6:
	ver_list.append(True)
else:
	ver_list.append(False)

time.sleep(60*15)

r_clear = requests.post("http://localhost:9000", json = data_normal)

get3 = requests.get("http://localhost:9000/healthz")

time.sleep(0.3)

print(get3.text)

if len(get2.text.split("|"))==1:
	ver_list.append(True)
else:
	ver_list.append(False)

print(ver_list)

#print(get.text.split("|") )

#wait 15 min
# time.sleep(60*15)