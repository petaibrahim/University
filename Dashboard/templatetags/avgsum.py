from django import template
register=template.Library()

@register.simple_tag
def best_avg(ct1=0,ct2=0,ct3=0,ct4=0):
    total=0
    count=0
    
    try:
        if ct1>0:
            count=count+1
    except:
        ct1=0
    try:        
        if ct2>0:
            count=count+1
    except:
        ct2=0
    try:
        if ct3>0:
            count=count+1
    except:
        ct3=0
    try:
        if ct4>0:
            count=count+1
    except:
        ct4=0

    if count>2:
        count=3
    
    return round(sum(sorted([ct1,ct2,ct3,ct4],reverse=True)[:3])/count)
    # return ct1


@register.simple_tag
def best_sum(attn=0,assign=0,ct1=0,ct2=0,ct3=0,ct4=0):
    # try:
    #     if ct1>0:
    #         count=count+1
    # except:
    #     ct1=0
    # try:        
    #     if ct2>0:
    #         count=count+1
    # except:
    #     ct2=0
    # try:
    #     if ct3>0:
    #         count=count+1
    # except:
    #     ct3=0
    # try:
    #     if ct4>0:
    #         count=count+1
    # except:
    #     ct4=0

    
    return int(best_avg(ct1,ct2,ct3,ct4))+attn+assign
    # return ct2