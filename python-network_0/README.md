0. cURL body size
mandatory
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

The size must be displayed in bytes
You have to use curl
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-network_0
File: 0-body_size.sh
 
0/6 pts
1. cURL to the end
mandatory
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

Display only body of a 200 status code response
You have to use curl
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-network_0
File: 1-body.sh
 
0/6 pts
2. cURL Method
mandatory
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

You have to use curl
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-network_0
File: 2-delete.sh
 
0/6 pts
3. cURL only methods
mandatory
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

You have to use curl
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-network_0
File: 3-methods.sh
 
0/6 pts
4. cURL headers
mandatory
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

A header variable X-HolbertonSchool-User-Id must be sent with the value 98
You have to use curl
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-network_0
File: 4-header.sh
 
0/6 pts
5. cURL POST parameters
mandatory
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

A variable email must be sent with the value test@gmail.com
A variable subject must be sent with the value I will always be here for PLD
You have to use curl
Please test your script in the container provided, using the web server running on port 5000

guillaume@ubuntu:~/$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alu-higher_level_programming
Directory: python-network_0
File: 5-post_params.sh
