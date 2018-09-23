from django import template
register=template.Library()

@register.simple_tag
def best_avg(ct1=0,ct2=0,ct3=0,ct4=0):
    total=0
    count=0
    
    if ct1>0:
        count=count+1
    if ct2>0:
        count=count+1
    if ct3>0:
        count=count+1
    if ct4>0:
        count=count+1
    if count>2:
        count=3
    
    return sum(sorted([ct1,ct2,ct3,ct4],reverse=True)[:3])/count
    # return ct1


@register.simple_tag
def best_sum(attn=0,assign=0,ct1=0,ct2=0,ct3=0,ct4=0):
    

    
    return sum(sorted([ct1,ct2,ct3,ct4],reverse=True)[:3])+attn+assign
    # return ct2