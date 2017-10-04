#pace_activityCode.py

'''
variables needed:

Job Number | string | if NULL, assume P70470 (standard AppSupp ticket)
Part Number | string | if NULL, assume 1
Activity Code | string | if NULL assume???
Notes (string) | string | if NULL assume???

login to pace
http://pace.westcanadian.com/epace/company:public/object/JobCost/addFromDC/1042
job box = id="d2639646e244"
part dropdown box = name="JobPartKey" id="d2639646e276"
activity code dropdown box = name="activityCode" id="d2639646e300"
notes box = name="notes" id="d2639646e404"
    NOTE:   box appears AFTER activity code is selected
            This should also follow this:
            #support_ticket_id# - #notes#
click submit = name="updateForm" type="submit"
    NOTE: the box has an onclick script
'''
