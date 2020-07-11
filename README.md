# UpgradeMe

This programs allows you to generate a boarding pass barcode from an image. 

> DISCLAIMER : Only for educational or some research purpose of course

## Install 

```bash
# First you need to build the container : 
docker build -t upgradeMe:v1 . 
# Then launch it bind your 8080 port to the container one : 
docker run -d -p 8080:8080 upgradeMe:v1
```
Then just go on your browser on `0.0.0.0:8080`upload you barcode and send it.   
You will get a new one upgraded !

## Flying company supported 

I don't do much OSINT so I did this program only with my last boarding pass. That is why I only got informations on Luftansa yet.  

Feel free to add more company codes in `codes.yaml`

- Luftansa

## Todo 

- Secure the code
- Add more companies
- Allow users to just change their information such as seat number, name etc by themselves. 
