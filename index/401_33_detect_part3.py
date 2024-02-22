#!/usr/bin/env python3

# Script Name:                  Challenge 33 Event Logging part 3/3
# Author Name:                  Nathalie Abdallah
# Date of latest revision:      02/21/2023
# Sources:                      https://chat.openai.com/, https://github.com/codefellows/seattle-ops-301d10
# Purpose:                      Objectives

import os
import hashlib
from datetime import datetime
from virustotal_python import Virustotal
from pprint import pprint
import time

# Initialize the VirusTotal API client
VIRUSTOTAL_API_KEY = 'api_key_here'
vtotal = Virustotal(API_KEY=VIRUSTOTAL_API_KEY)
