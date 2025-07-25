use curve25519_dalek::constants::X25519_BASEPOINT;
use curve25519_dalek::montgomery::MontgomeryPoint;
use curve25519_dalek::scalar::clamp_integer;

pub fn crypto_scalarmult(q: &mut [u8; 32], n: &[u8; 32], p: &[u8; 32]) {
    // Use the clamp_integer function from dalek
    let clamped = clamp_integer(*n);
    let point = MontgomeryPoint(*p);
    let result = point.mul_clamped(clamped);
    q.copy_from_slice(result.as_bytes());
}

pub fn crypto_scalarmult_base(q: &mut [u8; 32], n: &[u8; 32]) {
    // Use the X25519 basepoint and clamped multiplication
    let clamped = clamp_integer(*n);
    let result = X25519_BASEPOINT.mul_clamped(clamped);
    q.copy_from_slice(result.as_bytes());
}

#[no_mangle]
pub extern "C" fn crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult(
    q: *mut u8,
    n: *const u8,
    p: *const u8,
) -> i32 {
    unsafe {
        let q = &mut *(q as *mut [u8; 32]);
        let n = &*(n as *const [u8; 32]);
        let p = &*(p as *const [u8; 32]);
        crypto_scalarmult(q, n, p);
    }
    0
}

#[no_mangle]
pub extern "C" fn crypto_scalarmult_curve25519_rust_crypto_crypto_scalarmult_base(
    q: *mut u8,
    n: *const u8,
) -> i32 {
    unsafe {
        let q = &mut *(q as *mut [u8; 32]);
        let n = &*(n as *const [u8; 32]);
        crypto_scalarmult_base(q, n);
    }
    0
}
