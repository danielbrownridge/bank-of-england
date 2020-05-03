# Server Certificate Error

I get an error in my Chrome web browser when visiting a website that presents the below server certificate. Can you identify any issues with the certificate that may have caused this? Please briefly explain how you analysed this issue.

    -----BEGIN CERTIFICATE-----
    MIICXTCCAcYCCQDYpauf4ASdgTANBgkqhkiG9w0BAQQFADBzMQswCQYDVQQGEwJV
    SzEXMBUGA1UECAwOR3JlYXRlciBMb25kb24xDzANBgNVBAcMBkxvbmRvbjEYMBYG
    A1UECgwPQmFuayBvZiBFbmdsYW5kMSAwHgYDVQQDDBd3d3cuYmFua29mZW5nbGFu
    ZC5jby51azAeFw0yMDA0MTUxMjQ4MTdaFw0zMDA0MTMxMjQ4MTdaMHMxCzAJBgNV
    BAYTAlVLMRcwFQYDVQQIDA5HcmVhdGVyIExvbmRvbjEPMA0GA1UEBwwGTG9uZG9u
    MRgwFgYDVQQKDA9CYW5rIG9mIEVuZ2xhbmQxIDAeBgNVBAMMF3d3dy5iYW5rb2Zl
    bmdsYW5kLmNvLnVrMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDRQ0ZCROCc
    U8eKln5K0vAkloDZPm8OQMxUeU6BJ4NgyafCeLBuL9Ho8RU7MJGmrkwlmNuCKx8E
    /qENhfPPY1SHfNNQONVEGpyMvcS11PJB4QaSF2XkLT/fgfelud4AnOX/j01pUnkR
    Z8SRCder8jhmekGfoolWbot8kOO7X+gmPwIDAQABMA0GCSqGSIb3DQEBBAUAA4GB
    AHD57HcAWvF7IuE8yEh4ae5OpmSAFbbOO91JxBKDN8WA/HrEvLicNT8luu7gV7U6
    nTmL8q076XnEt0F4G8Slqi0xpmoo4VIOoEolwwT3eZ7mgDo5ddQL51dWf4q22fwK
    YV1oTphmKEy1w2k8Th4MJZy5m5uUGVTjb5StQChWZIGV
    -----END CERTIFICATE-----

## Answer

The certificate is issued by the same organisation it is intended for which means it is **self signed**. A valid certificate should issued by one of the trusted Certificate Authorities known to Google Chrome.


## Analysis
1. The data starts and ends with
`-----BEGIN CERTIFICATE-----`, end with `-----END CERTIFICATE-----` and has a base-64 encoded portion in the middle which implies that the data is a textual encoding of a **Public-Key Infrastructure X.509 (PKIX) certificate** ([RFC 7468 - 2. General Considerations](https://tools.ietf.org/html/rfc7468#section-2))

1. The certificate data is saved to a file `server.crt` to indicate that it is a certificate. The file extention `.crt` is used according to the recommendation _"...the extension ".crt"
   SHOULD be used for the textual encoding of a certificate..."_ ([RFC 7468 - 5.3. File Extension](https://tools.ietf.org/html/rfc7468#section-5.3))

1. To display certificate information for a PKIX certificate, the **x509** command can be used from the **openssl** toolkit. Options used are:

    * `-in server.crt` specifies the file to be read is *server.crt*
    * `-text` to print out the certificate information in text form
    * `-noout` to suppress output of the certificated in encoded form (which we already know)

    Output:
    
    ```bash
    $ openssl x509 -in server.crt -text -noout
     Certificate:
     Data:
         Version: 1 (0x0)
         Serial Number:
             d8:a5:ab:9f:e0:04:9d:81
         Signature Algorithm: md5WithRSAEncryption
         Issuer: C = UK, ST = Greater London, L = London, O = Bank of England, CN = www.bankofengland.co.uk
         Validity
             Not Before: Apr 15 12:48:17 2020 GMT
             Not After : Apr 13 12:48:17 2030 GMT
         Subject: C = UK, ST = Greater London, L = London, O = Bank of England, CN = www.bankofengland.co.uk
         Subject Public Key Info:
             Public Key Algorithm: rsaEncryption
                 RSA Public-Key: (1024 bit)
                 Modulus:
                     00:d1:43:46:42:44:e0:9c:53:c7:8a:96:7e:4a:d2:
                     f0:24:96:80:d9:3e:6f:0e:40:cc:54:79:4e:81:27:
                     83:60:c9:a7:c2:78:b0:6e:2f:d1:e8:f1:15:3b:30:
                     91:a6:ae:4c:25:98:db:82:2b:1f:04:fe:a1:0d:85:
                     f3:cf:63:54:87:7c:d3:50:38:d5:44:1a:9c:8c:bd:
                     c4:b5:d4:f2:41:e1:06:92:17:65:e4:2d:3f:df:81:
                     f7:a5:b9:de:00:9c:e5:ff:8f:4d:69:52:79:11:67:
                     c4:91:09:d7:ab:f2:38:66:7a:41:9f:a2:89:56:6e:
                     8b:7c:90:e3:bb:5f:e8:26:3f
                 Exponent: 65537 (0x10001)
     Signature Algorithm: md5WithRSAEncryption
          70:f9:ec:77:00:5a:f1:7b:22:e1:3c:c8:48:78:69:ee:4e:a6:
          64:80:15:b6:ce:3b:dd:49:c4:12:83:37:c5:80:fc:7a:c4:bc:
          b8:9c:35:3f:25:ba:ee:e0:57:b5:3a:9d:39:8b:f2:ad:3b:e9:
          79:c4:b7:41:78:1b:c4:a5:aa:2d:31:a6:6a:28:e1:52:0e:a0:
          4a:25:c3:04:f7:79:9e:e6:80:3a:39:75:d4:0b:e7:57:56:7f:
          8a:b6:d9:fc:0a:61:5d:68:4e:98:66:28:4c:b5:c3:69:3c:4e:
          1e:0c:25:9c:b9:9b:9b:94:19:54:e3:6f:94:ad:40:28:56:64:
          81:95
    ```

    From the above output we can observe a few things:
    
    * The command ran without error and gave output which shows that the certificate is structurally valid.
    * The period of validity for the certificate is between Apr 15 12:48:17 2020 GMT and Apr 13 12:48:17 2030 GMT so it is current and not expired.
    * The subject of the certificate is `www.bankofengland.co.uk` so it is clear that the intended use for this certificate is the Bank of England's website.
    * The issuer of the certificate is also the Bank of England. This means the subject and the issuer of the certificate are the same organisation which implies that the certificate is _self-signed_. This will not be accepted by modern web browsers.

1. To confirm the validity of the certificate the **verify** command from the **openssl** toolkit can also be used.

    ```bash
    $ openssl verify -extended_crl server.crt 
    C = UK, ST = Greater London, L = London, O = Bank of England, CN = www.bankofengland.co.uk
    error 18 at 0 depth lookup: self signed certificate
    error server.crt: verification failed
    ```


    This command yields the error `error 18 at 0 depth lookup: self signed certificate` which confirms that this is a self signed certificate and therefore not valid for production use.

1. If this certificate was used for a site the Chrome web browser would likely error with `NET:ERR_CERT_AUTHORITY_INVALID` because only certificates which are signed by the Certificate Authorities (CA) which are listed in the browser are accepted. These can be confirmed by visiting [chrome://settings/certificates](chrome://settings/certificates) and looking at the **Authorities**  tab. It can be seen that the Bank of England does not feature in this list as a CA.

1. A valid certificate would need to be signed by a recognised CA. The **s_client** command from **openssl** toolkit can be used to check the issuer real valid certificate for **www.bankofengland.co.uk**:

    ```bash
    $ openssl s_client -showcerts www.bankofengland.co.uk:443 </dev/null 2>/dev/null | openssl x509 --issuer --noout
    issuer=C = US, O = DigiCert Inc, CN = DigiCert SHA2 Secure Server CA
    ```

    This reveals that the issuer for the real certificate is **DigiCert SHA2 Secure Server CA** which is in the Authorities list in Google Chrome.


