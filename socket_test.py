# -*- coding: utf-8 -*-
#!/usr/bin/python

import urllib


# #################################################
# Routine to send the information to the prim
#     submitInformation(url,information)
#
def submitInformation(url,parameters) :
    # Set the parameters to be sent.
    encodedParams =  urllib.parse.urlencode(parameters).encode("utf-8");

    # Post the data.
    net = urllib.request.urlopen(url,encodedParams);

    # return the result.
    return(net.read());



if __name__ == "__main__":

    # Set the URL manually
    url = 'http://hydra.cs.fsu.edu:9000/lslhttp/63cead10-d75b-4d42-8677-7e8467c4657e/';

    # Define the parameters
    parameters = {'id':'244195d6-c9b7-4fd6-9229-c3a8b2e60e81',
                  'name':'M Linden'}

    # Pass the information along to the prim
    info = submitInformation(url,parameters);
    print(info);
