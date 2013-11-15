import win32com.client
 
o = win32com.client.Dispatch("Outlook.Application")
   
Msg = o.CreateItem(0)
Msg.To = "john@xxx.com"
   
Msg.CC = "john@xxx.com"
#Msg.BCC = "more email addresses here"
   
Msg.Subject = "The subject of you mail"
Msg.Body = "The main body text of you mail"
   
#attachment1 = "Path to attachment no. 1"
#attachment2 = "Path to attachment no. 2"
#Msg.Attachments.Add(attachment1)
#Msg.Attachments.Add(attachment2)
 
Msg.Send()

# import win32com.client as win32

# olook=win32.gencache.EnsureDispatch('outlook.Application')
# ns=olook.GetNamespace('MAPI')
# obox=ns.GetDefaultFolder(win32.constants.olFolderSentMail)

# obox.Items.Item(1).Display()
# print obox.Items.Item(1)#.Display()

# print obox.Items.Count
# print obox.Items.Item(8).SenderEmailAddress
# print obox.Items.Item(8).SenderName
# print obox.Items.Item(8).To
# print obox.Items.Item(8).Subject
# print obox.Items.Item(8).Body

# for i in range(1,obox.Items.Count):
    # print obox.Items.Item(i).SentOn,
