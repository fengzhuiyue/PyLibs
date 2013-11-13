#this function is used to get the uninstall string of a software in windows
#input:the dir which is a register key,the name of software product
#output:the uninstall string,if None,means no find  
def getProductCode(dir,prodcutName):
    uninstallString = ''
    
    #get the key of the uninstall path
    #get the subkey,get the one which have the same name with productName
    #by the subkey,get the value of uninstall string of it
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE ,dir)
        j=0
        while 1:
            name = _winreg.EnumKey(key,j)
            #name = repr(name) 
            
            path = dir + '\\' + name

            subkey = _winreg.OpenKey(key ,name)
            value,type ='',''
            try:
                value,type = _winreg.QueryValueEx(subkey,'DisplayName')
            except Exception,e:
                pass
            
            if value == prodcutName:
                try:
                    value2,type2 = _winreg.QueryValueEx(subkey,'UninstallString')
                except Exception,e:
                    pass
                uninstallString = value2
                return uninstallString
            _winreg.CloseKey(subkey)
            #print value,'    ',type
            j+=1    

    except WindowsError,e:
        print 
    finally:
        _winreg.CloseKey(key)
pass

#define the function uninstall_productbyCode(),to uninstall the product by code
def uninstall_productbyCode(code):
    #uninstall_cmd = "msiexec  /x /quiet /norestart " + path
    uninstall_cmd = code + '  /quiet'
    print uninstall_cmd
    if os.system(uninstall_cmd) == 0:
        return 0;
    else:
        return -1;

#define the function install_product(),to install the product
def install_product(path):
    install_cmd = "msiexec /qn /i " + path
    print install_cmd
    if os.system(install_cmd) == 0:
        return 0;
    else:
        return -1;

#define the function Is64Windows(),to judge the system is whether 64Windows
def Is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ


#define the function agent_install(),to auto install product     
def product_install():
if Is64Windows():
        product_path = product_loc + "softwarename_x64.msi"
    else:
        product_path = product_loc + "softwarename.msi"

    reg_dir = cst_path4_x86
    uninstallString = getProductCode(reg_dir,u'软件中文名')
    print uninstallString
    #for maybe in english system,we need to get english version product code,if we don't get chinese of that
    if uninstallString == None:
        uninstallString = getProductCode(reg_dir,u'软件英文名')
        print uninstallString
    # uninstall product
    if uninstallString != None and 0 == uninstall_productbyCode(uninstallString):
        print "uninstall softwarename scuessful"
    else:
        print "uninstall softwarename fail"

    # install product
    if 0 == install_product(product_path):
        print "install softwarename scuessful"
    else:
        print "install softwarename fail"
pass
