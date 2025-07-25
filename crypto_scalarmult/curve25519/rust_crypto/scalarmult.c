#include "crypto_scalarmult.h"

// Declare the Rust functions
extern int crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult(unsigned char *q,
  const unsigned char *n,
  const unsigned char *p);

extern int crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult_base(unsigned char *q,
  const unsigned char *n);

int crypto_scalarmult(unsigned char *q,
  const unsigned char *n,
  const unsigned char *p)
{
  crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult(q, n, p);
  return 0;
}

int crypto_scalarmult_base(unsigned char *q, const unsigned char *n)
{
  crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult_base(q, n);
  return 0;
}