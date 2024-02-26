description = "Simple web server version identifier"

author = "Nathalie"

license = "Same as Nmap--See https://nmap.org/book/man-legal.html"

categories = {"safe", "discovery"}

portrule = function(host, port)
    return port.protocol == "tcp" and port.number == 80
end

action = function(host, port)
    local socket = nmap.new_socket()
    local catch = function() socket:close() end
    local try = nmap.new_try(catch)
    socket:connect(host.ip, port.number)
    socket:send("GET / HTTP/1.0\r\nHost: " .. host.targetname .. "\r\n\r\n")
    local response = ""
    local status, data = socket:receive()
    while status do
        response = response .. data
        status, data = socket:receive()
    end
    socket:close()
    local server_header = response:match("^Server: ([^\r\n]+)")
    if server_header then
        return "Server header: " .. server_header
    else
        return "Server header not found"
    end
end
