import xml.etree.ElementTree as ET

def load_xml_file(fileName):
    root = ET.parse(fileName).getroot()
 
	#获取文件描述
	testsuite_name = root.find('testsuite name').text
	print testsuite_name
 
	#获取所有list节点
	all_testcase = root.findall('testcase')
 
	#遍历testcase节点的子元素
	for testcase in all_all_testcase:
		internalid = testcase.find('internalid').text       #得到head节点的文本
		actions = testcase.find('actions').text    #得到name节点的文本
		expectedresults = user.find('expectedresults').text     #得到sex节点的文本
		print internalid,actions,expectedresults
 
if __name__ == '__main__':
	load_xml_file('all_testsuites.xml')
