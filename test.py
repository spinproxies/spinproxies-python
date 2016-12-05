from spinproxies import SpinProxies


params = {}
params['key'] = 'my-api-key'
params['country_code'] = 'US,DE'
params['type'] = 'elite'
params['protocols'] = 'http'
params['format'] = 'txt'

#Initialize wrapper with the params
sp = SpinProxies(params)

#Test proxy list API endpoint
print(sp.proxy_list())

#Test proxy rotate API endpoint
print(sp.proxy_rotate())

