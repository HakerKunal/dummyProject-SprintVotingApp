import jwt


class EncodeDecodeToken:
    """
    for Encoding and decoding the userid into token
    """

    @staticmethod
    def encode_token(payload):
        encoded_token = jwt.encode({"user_id": payload},
                                   "secret",
                                   algorithm="HS256"
                                   )
        return encoded_token

    @staticmethod
    def decode_token(token):
        decoded_token = jwt.decode(token,
                                   "secret",
                                   algorithms="HS256"
                                   )
        return decoded_token
