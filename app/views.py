from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

# import digitaldivide.src.digitaldivideutil
# import digitaldivide.src.digitaldivide as digitaldivide



def index(request):
    return HttpResponse("Main Page.")

def get_result(request):
    # output_dump = digitaldivide.src.digitaldivideutil.digitaldividefunc()
    # hset = digitaldivide.HouseholdSet('digitaldivide\dat\household-internet-data.csv').sample()
    # (rowindex, h) = next(hset.iterrows())
    # house = digitaldivide.Household(h)
    output_dump='output'
    #output_dump +=   '''
    #Selected household ''' + str(house.unit_id) + ''' has the following characteristics:
    #Plan:  (Mbps down/up)'''+ str(house.advertised_rate_down)+" "+ str(house.advertised_rate_up)+ str(house.isp)+ str(house.technology)+ str(house.state)+'''--------------------------------------------------------'''
    # '''Estimated price per month: $'''+ house.monthly_charge.to_string()
    #  '''Upload rate (kbps)  '''+house.rate_up_kbps.to_string()
    # '''Download rate (kbps) '''+ house.rate_down_kbps.to_string()
    #  '''Round-trip delay (ms) | '''+ house.latency_ms.to_string()
    # '''Uplink jitter (ms)    | '''+house.jitter_up_ms.to_string()
    #  '''Downlink jitter (ms)   '''+ house.jitter_down_ms.to_string()
    # '''Packet loss (%%)       |'''+house.loss.to_string()
    #output_dump += str(dir(house))
    # output_dump += house.netem_template_up("192.168.0.1")
    return render(
        request,
        'page1.html',
        {
            'output_dump': output_dump
        }
    )
