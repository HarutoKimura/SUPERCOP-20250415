#include "api.h"

extern int crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult_base(
    unsigned char *q,
    const unsigned char *n
);

int crypto_scalarmult_base(unsigned char *q, const unsigned char *n)
{
    return crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult_base(q, n);
}