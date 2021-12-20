from pick import pick
import aws_boto as awsboto
title = 'Please choose the aws resource: '
options = ['ec2_state', 'List_Bucket_&_Object', 'Total_Bucket', 'Total_Account', 'Total_Lambda', 'List_Resources', 'ec2_running']
option= pick(options)
print(option[0])
#switcher = {
#    ec2_state: print(awsboto.ec2_state()),
#    List_Bucket_&_Object: "one",
#    Total_Bucket: "two",
#    Total_Account: "3",
#    Total_Lambda: "4",
#    ec2_running: "5",
#}
if option[0] == "ec2_state":
    print(awsboto.ec2_state())
elif option[0] == "List_Bucket_&_Object":
    print(awsboto.list_bkt_obj())   
elif option[0] == "Total_Bucket":
    print(awsboto.total_bucket())
elif option[0] == "Total_Account":
    print(awsboto.list_account())
elif option[0] == "Total_Lambda":
    print(awsboto.total_lambda()) 
elif option[0] == "List_Resources":
    print(awsboto.list_used_resource())
else:
    print(awsboto.ec2_running_state())
          
    