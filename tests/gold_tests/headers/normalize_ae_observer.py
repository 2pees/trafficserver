'''
Extract the protocol information from the Accept-Encoding headers and store it in a log file for later verification.
'''
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

log = open('normalize_ae.log', 'w')

def observe(headers):

    seen = False
    for h in headers.items():
        if h[0] == "X-Au-Test":
            log.write("X-Au-Test: {}\n".format(h[1]))

        if h[0] == "Accept-Encoding":
            log.write("{}\n".format(h[1]))
            seen = True

    if not seen:
        log.write("ACCEPT-ENCODING MISSING\n")

    log.write("-\n")
    log.flush()

Hooks.register(Hooks.ReadRequestHook, observe)
