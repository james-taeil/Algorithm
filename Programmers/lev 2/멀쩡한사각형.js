const gcd = (w, h) => {
    const mod = w % h;
    
    if(mod === 0) return h;
    return gcd(h, mod);
}

const solution = (w, h) => {
    const gcdValue = gcd(w, h);
    return w * h - (w + h - gcdValue);
}