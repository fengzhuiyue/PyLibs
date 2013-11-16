#############################################################################
# Software Testing Automation Framework (STAF)                              #
# (C) Copyright IBM Corp. 2001, 2005                                        #
#                                                                           #
# This software is licensed under the Eclipse Public License (EPL) V1.0.    #
#############################################################################

# This file contains tests for the STAF Python support
from PySTAF import *
from PySTAFMon import *
from PySTAFLog import *
import string
import sys

##############################################
# Test the STAFHandle and STAFResult classes #
##############################################

print "Testing the STAFHandle constructor"

# Verify get error if specify an integer for handle name when
# registering using a static STAF Handle

typeError = 0

try:
    handle = STAFHandle(1)
except STAFException, e:
    print "Error registering with STAF, RC: %d, Result: %s" % (e.rc, e.result)
    sys.exit(e.rc)
except TypeError, e:
    typeError = 1
    #print "Got expected TypeError: %s" % (e)

if typeError != 1:
    print "Did not get expected TypeError when specifying an invalid handle name"
    sys.exit(1)

# Verify get error if specify a non-integer for handle number when
# registering using a static STAF Handle

typeError = 0

try:
    handle = STAFHandle("MyHandle", STAFHandle.Static)
except STAFException, e:
    print "Error registering with STAF, RC: %d, Result: %s" % (e.rc, e.result)
    sys.exit(e.rc)
except TypeError, e:
    typeError = 1
    #print "Got expected Type Error: %s" % (e)

if typeError != 1:
    print "Did not get expected TypeError when specifying an invalid handle number"
    sys.exit(1)

# Verify creating a standard handle works and then use it to submit requests

print "Testing creating a standard handle and using it to submit requests"

try:
    handle = STAFHandle("Lang/Python/Test/Basic")
except STAFException, e:
    print "Error registering with STAF, RC: %d" % e.rc
    sys.exit(e.rc)

print "Using standard handle %d" % handle.handle

print "Testing submitting requests using a standard handle"

result = handle.submit("local", "ping", "ping")

if ((result.rc != STAFResult.Ok) or (result.result != "PONG")):
    print "Error on ping request."
    print "Expected RC: 0, Result: PONG"
    print "Received RC: %d, Result: %s" % (result.rc, result.result)
    sys.exit(1)

result = handle.submit("local", "var", "resolve string {STAF/Config/MachineNickname}")

if (result.rc != STAFResult.Ok):
    print "Error resolving machine nickname, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

self = result.result

# Verify creating a static handle works

print "Testing creating a reference to a static handle that exists"

result = handle.submit("local", "HANDLE", "CREATE HANDLE NAME TestPython");

if (result.rc != STAFResult.Ok):
    print "Error on create handle request."
    print "Expected RC: 0, Result: <A Number>"
    print "Received RC: %d, Result: %s" % (result.rc, result.result)
    sys.exit(1)

staticHandleNumber = int(result.result)

print "Using static handle %s" % (staticHandleNumber)

try:
    staticHandle = STAFHandle(staticHandleNumber, STAFHandle.Static)
except STAFException, e:
    print "Error registering a static handle with STAF, RC: %d" % e.rc
    sys.exit(e.rc)

if staticHandle.handle != staticHandleNumber:
    print "Invalid static handle number %s.  Expected %s." % \
          (staticHandle.handle, staticHandleNumber)
if staticHandle.handleType != STAFHandle.Static:
    print "Invalid handle type %s.  Expected %s." % \
          (staticHandle.handleType, STAFHandle.Static)

print "Testing submitting requests using a static handle"

result = staticHandle.submit("local", "PING", "PING")

if (result.rc != 0) or (result.result != "PONG"):
    print "Error submitting request, RC: %d, Result: %s" % (result.rc, result.result)
    sys.exit(result.rc)

# Verify doUnmarshallingResult defaults to 1 when creating a static handle

if staticHandle.getDoUnmarshallResult() != 1:
    print "ERROR: staticHandle.getDoUnmarshallResult() != 1"
    print 'Found: %s' % (staticHandle.getDoUnmarshallResult())
    sys.exit(1)

print "Unregister and delete static handle %s" % (staticHandleNumber)

try:
    staticHandle.unregister()
except STAFException, e:
    print "Error unregistering static handle with STAF, RC: %d" % e.rc
    sys.exit(e.rc)

result = handle.submit("local", "HANDLE", "DELETE HANDLE %s" % (staticHandleNumber))

if (result.rc != STAFResult.Ok):
    print "Error deleting static handle."
    print "Expected RC: 0"
    print "Received RC: %d, Result: %s" % (result.rc, result.result)
    sys.exit(1)

result = handle.submit("local", "HANDLE", "QUERY HANDLE %s" % (staticHandleNumber))

if (result.rc != STAFResult.HandleDoesNotExist):
    print "ERROR: Static handle %s still exists after being deleted."
    print "Expected RC: %s, Result: %s" % (STAFResult.HandleDoesNotExist, staticHandleNumber)
    print "Received RC: %d, Result: %s" % (result.rc, result.result)
    sys.exit(1)

print "\nVerify that auto-unmarshalling result is turned on by default"

# Test the STAFHandle.getDoUnmarshallResult API

if handle.getDoUnmarshallResult() != 1:
    print "ERROR: handle.getDoUnmarshallResult() != 1"
    print 'Found: %s' % (handle.getDoUnmarshallResult())
    sys.exit(1)

request = "WHOAMI"
result = handle.submit("local", "MISC", request)

if (result.rc != STAFResult.Ok):
    print "Error on MISC WHOAMI requst, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure that the resultContext and resultObj variables in the
# STAFResult class were set correctly since auto-unmarshalling result is on

if result.resultContext.getRootObject() != unmarshall(result.result).getRootObject():
    print 'STAFResult resultContext variable is not set correctly.'
    print 'Expected:\n%s' % (unmarshall(result.result))
    print 'Found:\n%s' % (result.resultContext)
    sys.exit(1)

if result.resultObj != unmarshall(result.result).getRootObject():
    print 'STAFResult resultObj variable is not set correctly.'
    print 'Expected:\n%s' % (unmarshall(result.result).getRootObject())
    print 'Found:\n%s' % (result.resultObj)
    sys.exit(1)

# Make sure that if turn off auto-unmarshalling result that the
# resultContext and resultObj variables are set to None since
# auto-unmarshalling result is off

# Test the STAFHandle.setDoUnmarshallResult API

print "Turn off auto-unmarshalling result"
handle.setDoUnmarshallResult(0)

if handle.getDoUnmarshallResult() != 0:
    print "ERROR: handle.getDoUnmarshallResult() != 0"
    print 'Found: %s' % (handle.getDoUnmarshallResult())
    sys.exit(1)

result = handle.submit("local", "MISC", request)

if (result.rc != STAFResult.Ok):
    print "Error on MISC WHOAMI requst, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

if result.resultContext != None:
    print 'STAFResult resultContext variable != None'
    print 'Found:\n%s' % (result.resultContext)
    sys.exit(1)

if result.resultObj != None:
    print 'STAFResult resultObj variable != None'
    print 'Found:\n%s' % (result.resultObj)
    sys.exit(1)

# Test if pass in any true value to setDoUnmarshallResult() that
# getDoUnmarshallResult returns 1

handle.setDoUnmarshallResult("true");

if handle.getDoUnmarshallResult() != 1:
    print "ERROR: handle.getDoUnmarshallResult() != 1"
    print 'Found: %s' % (handle.getDoUnmarshallResult())
    sys.exit(1)

# Test if pass in any false value to setDoUnmarshallResult() that
# getDoUnmarshallResult returns 0

handle.setDoUnmarshallResult("");

if handle.getDoUnmarshallResult() != 0:
    print "ERROR: handle.getDoUnmarshallResult() != 0"
    print 'Found: %s' % (handle.getDoUnmarshallResult())
    sys.exit(1)

# Make sure that if turn on auto-unmarshalling result that the
# resultContext and resultObj variables are set correctly since
# auto-unmarshalling result is on

print "Turn on auto-unmarshalling result"
handle.setDoUnmarshallResult(1)

if handle.getDoUnmarshallResult() != 1:
    print "ERROR: handle.getDoUnmarshallResult() != 1"
    print 'Found: %s' % (handle.getDoUnmarshallResult())
    sys.exit(1)

result = handle.submit("local", "MISC", request)

if (result.rc != STAFResult.Ok):
    print "Error on MISC WHOAMI requst, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure that the resultContext and resultObj variables in the
# STAFResult class were set correctly

if result.resultContext.getRootObject() != unmarshall(result.result).getRootObject():
    print 'STAFResult resultContext variable is not set correctly.'
    print 'Expected:\n%s' % (unmarshall(result.result))
    print 'Found:\n%s' % (result.resultContext)
    sys.exit(1)

if result.resultObj != unmarshall(result.result).getRootObject():
    print 'STAFResult resultObj variable is not set correctly.'
    print 'Expected:\n%s' % (unmarshall(result.result).getRootObject())
    print 'Found:\n%s' % (result.resultObj)
    sys.exit(1)

###############################################
# Next, lets test the monitor service wrapper #
###############################################

print "\nTesting Monitor service functions"

# Log the message

monitor = STAFMonitor(handle)
monitorMessage = "Hello World"

result = monitor.log(monitorMessage)

if (result.rc != STAFResult.Ok):
    print "Error on STAFMonitorDoLog, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Try to retrieve it

request = "query machine %s handle %d" % (self, handle.handle)
result = handle.submit("local", "monitor", request)

if (result.rc != STAFResult.Ok):
    print "Error querying monitor info, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure we got back the correct message

monitorMap = result.resultObj

if monitorMap['message'] != monitorMessage:
    print "Wrong output for MONITOR QUERY request"
    print "Expected to find:"
    print "{"
    print "  Date-Time: <Timestamp>"
    print "  Message  : %s" % (monitorMessage)
    print "}"
    print "Found:\n%s" % context
    sys.exit(1)

##############################################
# Finally, lets test the log service wrapper #
##############################################

print "Testing Log service functions"

logName = "PythonTest"

# Setup logging

log = STAFLog(handle, STAFLog.Handle, logName,
              [ STAFLog.Fatal, STAFLog.Error, STAFLog.Warning, STAFLog.Info ])

# Log the message

logMessage = "A log message"
result = log.log(STAFLog.Info, logMessage)

if (result.rc != STAFResult.Ok):
    print "Error on STAFLog.log(), RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Try to retrieve it

request = "query machine %s handle %d logname %s" % \
          (self, handle.handle, logName)
result = handle.submit("local", "log", request)

if (result.rc != STAFResult.Ok):
    print "Error on STAF LOG Service QUERY, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure we got back the correct message

logRecordList = result.resultObj

if (len(logRecordList) > 0 and
    logRecordList[len(logRecordList) - 1]['level'] == STAFLog.Info and
    logRecordList[len(logRecordList) - 1]['message'] == logMessage):
    logRecord = logRecordList[len(logRecordList) - 1]
else:
    print "Wrong output for log query request"
    print "Expected to find one record with level: '%s' and message: '%s'" % \
          (STAFLog.Info, logMessage)
    print "Found:\n'%s'" % context
    sys.exit(1)

# Try to retrieve it from monitor

request = "query machine %s handle %d" % (self, handle.handle)
result = handle.submit("local", "monitor", request)

if (result.rc != STAFResult.Ok):
    print "Error on querying monitor info, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure we got back the correct message from monitor

monitorMap = result.resultObj

if monitorMap['message'] != '%s:%s' % (STAFLog.Info, logMessage):
    print "Wrong output for MONITOR QUERY request"
    print "Expected to find:"
    print "{"
    print "  Date-Time: <Timestamp>"
    print "  Message  : %s:%s" % (STAFLog.Info, logMessage)
    print "}"
    print "Found:\n%s" % context
    sys.exit(1)

# Delete the log file

request = "delete machine %s handle %d logname %s confirm" % \
          (self, handle.handle, logName)
result = handle.submit("local", "log", request)

if (result.rc != STAFResult.Ok):
    print "Error deleting log file, RC: %s, Result: %s" % \
          (result.rc, result.result)
    sys.exit(1)

# Log the message so that Monitor shouldn't get it

result = log.log(STAFLog.Status, logMessage)

if (result.rc != STAFResult.Ok):
    print "Error on STAFLog.log(), RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Try to retrieve it

request = "query machine %s handle %d logname %s" % \
          (self, handle.handle, logName)
result = handle.submit("local", "log", request)

if (result.rc != STAFResult.Ok):
    print "Error on STAF LOG Service QUERY, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure we got back the correct message

logRecordList = result.resultObj

if (len(logRecordList) == 1 and
    logRecordList[0]['level'] == STAFLog.Status and
    logRecordList[0]['message'] == logMessage):
    logRecord = logRecordList[0]
else:
    print "Wrong output for log query request"
    print "Expected to find one record with level: '%s' and message: '%s'" % \
          (STAFLog.Status, logMessage)
    print "Found '%s'" % context
    sys.exit(1)

# Try to retrieve it from monitor

request = "query machine %s handle %d" % (self, handle.handle)
result = handle.submit("local", "monitor", request)

if (result.rc != STAFResult.Ok):
    print "Error on querying monitor info, RC: %d, Result: %s" % \
          (result.rc, result.result)
    sys.exit(result.rc)

# Make sure we got back the correct (old) message from monitor

monitorMap = result.resultObj

if monitorMap['message'] != '%s:%s' % (STAFLog.Info, logMessage):
    print "Wrong output for MONITOR QUERY request"
    print "Expected to find:"
    print "{"
    print "  Date-Time: <Timestamp>"
    print "  Message  : %s:%s" % (STAFLog.Info, logMessage)
    print "}"
    print "Found:\n%s" % context
    sys.exit(1)

# Delete the log file

request = "delete machine %s handle %d logname %s confirm" % \
          (self, handle.handle, logName)
result = handle.submit("local", "log", request)

if (result.rc != STAFResult.Ok):
    print "Error deleting log file, RC: %s, Result: %s" % \
          (result.rc, result.result)
    sys.exit(1)


########################################
# Next, test the marshall function     #
########################################

print "Testing marshall function"

myTestMap = {'name': 'TestA', 'exec': '/tests/TestA.py', 'testType': 'FVT', 'outputs': ['TestA.out', 'TestA.err']}
marshalledResult = marshall(myTestMap)
expectedResult = (
    "@SDT/{:138::7:outputs@SDT/[2:38:@SDT/$S:9:TestA.out" +
    "@SDT/$S:9:TestA.err:8:testType@SDT/$S:3:FVT:4:name" +
    "@SDT/$S:5:TestA:4:exec@SDT/$S:15:/tests/TestA.py")

if marshalledResult != expectedResult:
    print "Wrong output for marshall function"
    print "Expected to find:\n%s" % (expectedResult)
    print "Found:\n%s" % (marshalledResult)
    sys.exit(1)


#########################################
# Next, test the STAFMapClassDefinition #
#########################################

print "Testing STAFMapClassDefinition class"

mapClassDefName = 'Test/MyMap'

myMapClassDef = STAFMapClassDefinition(mapClassDefName)
myMapClassDef.addKey('name', 'Name')
myMapClassDef.addKey('exec', 'Executable')
myMapClassDef.addKey('testType', 'Test Type')
myMapClassDef.setKeyProperty('testType', 'display-short-name', 'test')
myMapClassDef.addKey('outputs', 'Outputs')

expectedKeyMap = [
  {'display-name': 'Name', 'key': 'name'},
  {'display-name': 'Executable', 'key': 'exec'},
  {'display-name': 'Test Type', 'key': 'testType', 'display-short-name': 'test'},
  {'display-name': 'Outputs', 'key': 'outputs'}
]

if myMapClassDef.keys() != expectedKeyMap:
    print "Wrong keys for myMapClassDef"
    print "Expected:\n%s" % (expectedKeyMap)
    print "Found:\n%s" % (myMapClassDef.keys())
    sys.exit(1)

if myMapClassDef.name() != mapClassDefName:
    print "Wrong name for myMapClassDef"
    print "Expected: %s" % (myClassDefName)
    print "Found   : %s" % (myMapClassDef.name())
    sys.exit(1)

expectedMapClass = {
  'keys': [
    {'display-name': 'Name', 'key': 'name'},
    {'display-name': 'Executable', 'key': 'exec'},
    {'display-name': 'Test Type', 'key': 'testType', 'display-short-name': 'test'},
    {'display-name': 'Outputs', 'key': 'outputs'}
  ],
  'name': 'Test/MyMap'
}

if myMapClassDef.getMapClassDefinitionObject() != expectedMapClass:
    print "getMapClassDefinitionObject() returned wrong object"
    print "Expected:\n%s" % (expectedMapClass)
    print "Found:\n%s" % (myMapClassDef.getMapClassDefinitionObject())
    sys.exit(1)

myMapClass = myMapClassDef.createInstance()

#########################################
# Next, test the STAFMarshallingContext #
#########################################

print "Testing STAFMarshallingContext class"

mc = STAFMarshallingContext()

mc.setMapClassDefinition(myMapClassDef)

theMapClassDef = mc.getMapClassDefinition('Test/MyMap')

if theMapClassDef.keys() != expectedKeyMap:
    print "Wrong keys for theMapClassDef"
    print "Expected:\n%s" % (expectedKeyMap)
    print "Found:\n%s" % (theMapClassDef.keys())
    sys.exit(1)

if theMapClassDef.getMapClassDefinitionObject() != expectedMapClass:
    print "Error: getMapClassDefinitionObject() returned wrong object"
    print "Expected:\n%s" % (expectedMapClass)
    print "Found:\n%s" % (theMapClassDef.getMapClassDefinitionObject())
    sys.exit(1)

if mc.hasMapClassDefinition('Test/MyMap') != 1:
    print "Error: The marshalling context does not have map class definition 'Test/MyMap'"
    sys.exit(1)

mc.setRootObject(myTestMap)
rootObj = mc.getRootObject()

if rootObj != myTestMap:
    print "Error: mc.getRootObject() returned wrong object"
    print "Expected:\n%s" % (myTestMap)
    print "Found:\n%s" % (rootObj)
    sys.exit(1)
    
if isMarshalledData('xyz'):
    print "Error: 'xyz' is not marshalled data"
    sys.exit(1)

if not mc.isMarshalledData(marshalledResult):
    print "Not marshalled data.  marshalledResult=%s" % (marshalledResult)
    sys.exit(1)

keyMap = mc.mapClassDefinitionIterator()
if len(keyMap) == 1 and keyMap[0] == 'Test/MyMap':
    print ''
else:
    print "Error: mc.mapClassDefinitionIterator() != ['Test/MapMap']"
    print "mc.mapClassDefinitionIterator()=%s" % mc.mapClassDefinitionIterator()
    sys.exit()

priObj = mc.getPrimaryObject()

if priObj != mc:
    print "Error: mc.getPrimaryObject() != mc"
    print "mc.getPrimaryObject()=%s" % (mc.getPrimaryObject())
    print "mc=%s" % (mc)
    sys.exit()

formattedOutput = '%s' % (mc)
formattedOutput1 = mc.__str__()
formattedOutput2 = mc.__repr__()
formattedOutput3 = formatObject(myTestMap, mc)

if (formattedOutput != formattedOutput1 or
    formattedOutput != formattedOutput2 or
    formattedOutput != formattedOutput3):
    print "Error in str(), repr(), or formatObject function"
    print "formattedOutput=%s" % (formattedOutput)
    print "formattedOutput1=%s" % (formattedOutput)
    print "formattedOutput2=%s" % (formattedOutput)
    print "formattedOutput3=%s" % (formattedOutput)
    sys.exit(1)

# Test the marshall function using a MapClassDefinition

expectedResult2 = (
    "@SDT/*:558:@SDT/{:398::13:map-class-map@SDT/{:370::10:Test/MyMap" +
    "@SDT/{:345::4:keys@SDT/[4:298:@SDT/{:50::12:display-name" +
    "@SDT/$S:4:Name:3:key@SDT/$S:4:name@SDT/{:57::12:display-name" +
    "@SDT/$S:10:Executable:3:key@SDT/$S:4:exec@SDT/{:95::12:display-name" +
    "@SDT/$S:9:Test Type:3:key@SDT/$S:8:testType:18:display-short-name" +
    "@SDT/$S:4:test@SDT/{:56::12:display-name@SDT/$S:7:Outputs:3:key" +
    "@SDT/$S:7:outputs:4:name@SDT/$S:10:Test/MyMap@SDT/{:138::7:outputs" +
    "@SDT/[2:38:@SDT/$S:9:TestA.out@SDT/$S:9:TestA.err:8:testType" +
    "@SDT/$S:3:FVT:4:name@SDT/$S:5:TestA:4:exec@SDT/$S:15:/tests/TestA.py")

marshalledResult2 = marshall(mc, mc)

if marshalledResult2 != expectedResult2:
    print "Error: Wrong output for marshall function"
    print "Expected to find:\n%s" % (expectedResult2)
    print "Found:\n%s" % (marshalledResult2)
    sys.exit(1)

marshalledResult3 = mc.marshall()

if marshalledResult3 != expectedResult2:
    print "Error: Wrong output for marshall function"
    print "Expected to find:\n%s" % (expectedResult2)
    print "Found:\n%s" % (marshalledResult3)
    sys.exit(1)

# Create a STAFMarshallingContext instance specifying the object
# and mapClassMap

mc2 = STAFMarshallingContext(myTestMap, mc.getMapClassMap())

if mc2.hasMapClassDefinition('Test/MyMap') != 1:
    print "Error: mc2 does not have map class definition 'Test/MyMap'"
    print "mc2=%s" % mc2
    sys.exit(1)

rootObj = mc2.getRootObject()

if rootObj != myTestMap:
    print "Error: mc2.getRootObject() returned wrong object"
    print "Expected:\n%s" % (myTestMap)
    print "Found:\n%s" % (rootObj)
    sys.exit(1)


########################################
# Next, test the unmarshall function   #
########################################

print "Testing unmarshall function"

# Unmarshall the marshalledResult

mc = unmarshall(marshalledResult)

if mc.getRootObject() != myTestMap:
    print 'Unmarshalled object not same as original object that was marshalled'
    print 'Expected:\n%s' % (myTestMap)
    print 'Found:\n%s' % (marshalledResult.getRootObject())
    sys.exit(1)

# Unmarshall the result from a FS QUERY ENTRY request

fileName = '{STAF/Config/ConfigFile}'

result = handle.submit('local', 'FS', 'QUERY ENTRY %s' % fileName)

if result.rc != STAFResult.Ok:
    print 'FS QUERY ENTRY %s failed' % fileName
    print 'RC=%s Result=%s' % (result.rc, result,result)
    sys.exit(1)

mc = unmarshall(result.result)
entryMap = mc.getRootObject()

if entryMap['type'] == 'F' and int(entryMap['lowerSize']) > 0 and entryMap['lastModifiedTimestamp']:
    print ''
else:
    print 'Unmarshall/getRootObject() failed'
    print "entryMap['type']=%s entryMap['lowerSize']=%s entryMap['lastModifiedTimestamp']=%s" % \
          (entryMap['type'], entryMap['lowerSize'], entryMap['lastModoifiedTimestamp'])

# Marshall a map and queue it; Get it off the queue, and unmarshall it
# and verify results in original map object that was marshalled

message = marshall(myTestMap)
result = handle.submit('local', 'QUEUE', 'QUEUE MESSAGE %s' % message)

if result.rc != STAFResult.Ok:
    print 'QUEUE MESSAGE failed with RC=%s Result=%s' % (result.rc, result.result)
    sys.exit(1)

# Another process could obtain the message from the queue and unmarshall
# it to get the original dictionary (map) object

result = handle.submit('local', 'QUEUE', 'GET MESSAGE')

if result.rc == STAFResult.Ok:
    mc = unmarshall(result.result)
    yourTestMap = mc.getRootObject()

############################################
# Next, test the formatObject function     #
############################################

print "Testing formatObject function\n"

print "Printing formatted output for %s" % (myTestMap)
print formatObject(myTestMap)

fileName = '{STAF/Config/ConfigFile}'

result = handle.submit('local', 'FS', 'QUERY ENTRY %s' % wrapData(fileName))

if result.rc != STAFResult.Ok:
    print 'FS QUERY ENTRY %s failed' % fileName
    print 'RC=%s Result=%s' % (result.rc, result,result)
    sys.exit(1)

print "Printing formatted output for FS QUERY ENTRY %s" % (fileName)
print formatObject(result.resultObj, result.resultContext)

# Create a marshalling context and marshall it, and unmarshall it

myMapClassDef = STAFMapClassDefinition('Test/MyMap')
myMapClassDef.addKey('name', 'Name')
myMapClassDef.addKey('exec', 'Executable')

testList = [
             {'name': 'TestA', 'exec': '/tests/TestA.py'},
             {'name': 'TestB', 'exec': '/tests/TestB.sh'},
             {'name': 'TestC', 'exec': '/tests/TestC.cmd'}
           ]

mc = STAFMarshallingContext()
mc.setMapClassDefinition(myMapClassDef)

myTestList = []

for test in testList:
    testMap = myMapClassDef.createInstance()
    testMap['name'] = test['name']
    testMap['exec'] = test['exec']
    myTestList.append(testMap)

mc.setRootObject(myTestList)
message = marshall(mc)
mc2 = unmarshall(message)
mc2.getRootObject()

if str(mc) != str(mc2):
    print "Error: str(mc) != str(mc2)"
    print "mc=%s" % mc
    print "mc2=%s" % mc2
    sys.exit(1)

mc3 = STAFMarshallingContext(mapClassMap=mc.getMapClassMap())
mc4 = STAFMarshallingContext(obj=myTestList, mapClassMap=mc.getMapClassMap())

# Test privacy methods

password = 'secret';
pwWithPD = STAFAddPrivacyDelimiters(password)
print 'STAFAddPrivacyDelimiters(%s)=%s' % (password, pwWithPD)
print 'STAFEscapePrivacyDelimiters(%s)=%s' % (pwWithPD, STAFEscapePrivacyDelimiters(pwWithPD))
print 'STAFMaskPrivateData(%s)=%s' % (pwWithPD, STAFMaskPrivateData(pwWithPD))
print 'STAFRemovePrivacyDelimiters(%s)=%s' % (pwWithPD, STAFRemovePrivacyDelimiters(pwWithPD))

password = 'secret';
pwWithPD = addPrivacyDelimiters(password)
print 'addPrivacyDelimiters(%s)=%s' % (password, pwWithPD)
print 'escapePrivacyDelimiters(%s)=%s' % (pwWithPD, escapePrivacyDelimiters(pwWithPD))
print 'maskPrivateData(%s)=%s' % (pwWithPD, maskPrivateData(pwWithPD))
print 'removePrivacyDelimiters(%s)=%s' % (pwWithPD, removePrivacyDelimiters(pwWithPD))

# Test private data methods

testData = ['secret', 'secret', '!!@secret@!!', 'Pw: !!@pw@!!', '^!!@secret@!!',
            '^!!@secret^@!!', '!!@secret', '!!@secret^@!!',
            'Pw1=%s, Pw2=%s.' % (addPrivacyDelimiters('a'), addPrivacyDelimiters('pw')),
            '^%s^%s' % (addPrivacyDelimiters('a'), addPrivacyDelimiters('b')),
            'Pw1=!!@secret, !!@pw@!!.', 'Pw1=!!@secret@!!, !!@pw.',
            'Msg: !!@Pw: ^!!@pw^@!!@!!', '@!!a!!@b@!!', '' ]
        
print ("KEY:\n  apd() = STAFUtil.addPrivacyDelimiters()\n" +
       "  mpd() = STAFUtil.maskPrivateData()\n" +
       "  rpd() = STAFUtil.removePrivacyDelimiters()\n" +
       "  epd() = STAFUtil.escapePrivacyDelimiters()\n")

numErrors = 0;

for i in range(0, len(testData)):
  data = testData[i]

  print '\n%s)  data: %s\n'  % ((i+1), data)

  maskedData2 = maskPrivateData(data)
  print "mpd(" + data + "): " + maskedData2 + "\n"

  dataWithPrivacy = addPrivacyDelimiters(data)
  print "apd(" + data + "): " + dataWithPrivacy

  dataWithPrivacyRemoved = removePrivacyDelimiters(dataWithPrivacy, 1)
  print "rpd(" + dataWithPrivacy + ", 1): " + dataWithPrivacyRemoved

  dataWithPrivacyRemoved2 = removePrivacyDelimiters(dataWithPrivacy, 2)
  print "rpd(" + dataWithPrivacy + ", 2): " + dataWithPrivacyRemoved2

  dataWithAllPrivacyRemoved = removePrivacyDelimiters(dataWithPrivacy, 0)
  print "rpd(" + dataWithPrivacy + ", 0): " + dataWithAllPrivacyRemoved

  escapedData = escapePrivacyDelimiters(data)
  print "\nepd(" + data + "): " + escapedData

  dataWithPrivacy = addPrivacyDelimiters(escapedData)
  print "apd(" + escapedData + "): " + dataWithPrivacy

  dataWithPrivacyRemoved = removePrivacyDelimiters(dataWithPrivacy, 1)
  print "rpd(" + dataWithPrivacy + ", 1): " + dataWithPrivacyRemoved

  if (dataWithPrivacyRemoved != data):
    print "ERROR: removePrivacyDelimiters(" + dataWithPrivacyRemoved + ", 1) != " + data
    numErrors = numErrors + 1
    print numErrors
    
  dataWithAllPrivacyRemoved = removePrivacyDelimiters(dataWithPrivacy)
  print "rpd(" + dataWithPrivacy + ", 0): " + dataWithAllPrivacyRemoved

  if (dataWithAllPrivacyRemoved != data):
    print "ERROR: removePrivacyDelimiters(" + dataWithAllPrivacyRemoved + ", 0) != " + data
    numErrors = numErrors + 1
    print numErrors
    
if (numErrors == 0):
  print "\n*** All tests successful ***"
else:
  print "\n*** ERROR: %s tests failed ***" % (numErrors)


#############
# Finish up #
#############

result = handle.unregister()

if (result != STAFResult.Ok):
    print "Error unregistering with STAF, RC: %d" % result
    sys.exit(result)
    
sys.exit(0)