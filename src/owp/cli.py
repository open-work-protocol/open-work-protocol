import argparse, json
from pathlib import Path
from .demo import run_demo
from .tck import run_vectors
from .simple_demo import run_simple_demo
from .golden import run_golden_journey

def main():
    parser=argparse.ArgumentParser(prog='owp')
    sub=parser.add_subparsers(dest='command',required=True)
    demo=sub.add_parser('demo'); demo.add_argument('--json',action='store_true')
    golden=sub.add_parser('golden-demo'); golden.add_argument('--json',action='store_true')
    simple=sub.add_parser('simple-demo'); simple.add_argument('--json',action='store_true')
    tck=sub.add_parser('tck'); tck.add_argument('--vectors',default=str(Path(__file__).resolve().parents[2]/'tck'/'vectors'))
    args=parser.parse_args()
    if args.command=='demo':
        result=run_demo(verbose=not args.json)
        if args.json: print(json.dumps(result,indent=2))
    elif args.command=='golden-demo':
        result=run_golden_journey()
        print(json.dumps(result,indent=2) if args.json else result)
    elif args.command=='simple-demo':
        result=run_simple_demo()
        print(json.dumps(result,indent=2) if args.json else result)
    elif args.command=='tck':
        passed,failures=run_vectors(args.vectors)
        print(f'OWP TCK: {passed} vectors passed')
        if failures:
            for f in failures: print('FAIL:',f)
            raise SystemExit(1)

if __name__=='__main__': main()
