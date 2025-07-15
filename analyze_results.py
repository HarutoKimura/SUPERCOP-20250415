#!/usr/bin/env python3
import re
import sys

def parse_benchmark_results(filename):
    results = []
    
    with open(filename, 'r') as f:
        for line in f:
            # Look for successful curve25519 benchmark lines
            if 'crypto_scalarmult/curve25519' in line and 'try' in line and 'ok' in line:
                # Find the 'ok' keyword and extract cycles after it
                ok_index = line.find(' ok ')
                if ok_index != -1:
                    after_ok = line[ok_index + 4:].strip().split()
                    if len(after_ok) >= 3:
                        try:
                            cycles = int(after_ok[0])  # First number after 'ok'
                            
                            # Extract implementation name
                            impl_match = re.search(r'crypto_scalarmult/curve25519/([^/\s]+)', line)
                            impl_name = impl_match.group(1) if impl_match else "unknown"
                            
                            # Extract compiler info (look for gcc_ or clang_)
                            compiler_match = re.search(r'(gcc_[^\s]+|clang_[^\s]+)', line)
                            compiler = compiler_match.group(1) if compiler_match else "unknown"
                            
                            # Clean up compiler info
                            compiler_clean = compiler.replace('_', ' ').replace('-', ' ')
                            
                            results.append({
                                'cycles': cycles,
                                'implementation': impl_name,
                                'compiler': compiler_clean,
                                'full_line': line.strip()
                            })
                        except ValueError:
                            continue
    
    return results

def main():
    filename = 'bench/sapporo/data'
    results = parse_benchmark_results(filename)
    
    if not results:
        print("No benchmark results found!")
        return
    
    # Sort by cycles (lower is better)
    results.sort(key=lambda x: x['cycles'])
    
    print("=== TOP 15 CURVE25519 IMPLEMENTATIONS BY PERFORMANCE ===")
    print(f"{'Rank':<4} {'Cycles':<12} {'Implementation':<15} {'Compiler'}")
    print("-" * 80)
    
    for i, result in enumerate(results[:15]):
        print(f"{i+1:<4} {result['cycles']:<12,} {result['implementation']:<15} {result['compiler'][:50]}")
    
    print(f"\nTotal implementations tested: {len(results)}")
    
    # Group by implementation
    impl_best = {}
    for result in results:
        impl = result['implementation']
        if impl not in impl_best or result['cycles'] < impl_best[impl]['cycles']:
            impl_best[impl] = result
    
    print("\n=== BEST RESULT PER IMPLEMENTATION ===")
    print(f"{'Implementation':<15} {'Best Cycles':<12} {'Compiler'}")
    print("-" * 70)
    
    for impl, result in sorted(impl_best.items(), key=lambda x: x[1]['cycles']):
        print(f"{impl:<15} {result['cycles']:<12,} {result['compiler'][:40]}")

if __name__ == "__main__":
    main() 