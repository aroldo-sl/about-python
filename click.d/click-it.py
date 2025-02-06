#!/usr/bin/env python
import click
import json
import pprint

'''
Von "https://www.assemblyai.com/blog/the-definitive-guide-to-python-click/"
@click.group(<name>) creates a command that instantiates a group class
a group is intended to be a set of related commands
@click.argument(<argument name>) tells us that we will be passing an argument
and referring to that argument in the function by the name we pass it
@click.pass_context tells the group command that we're going to be using
the context, the context is not visible to the command unless we pass this
 
In our example we'll name our group "cli"
'''

#
@click.group("Rumpelstilzchen")
@click.pass_context
@click.argument("document")
def do_things(ctx, document = None):
   """An example CLI for interfacing with a document"""
   if document is None:
      document = "formatted-messages.json"
   _stream = open(document)
   _dict = json.load(_stream)
   _stream.close()
   ctx.obj = _dict

@Rumpelstilzchen.command("check")
def check_context_object(ctx):
   

   
#
def main():
    """
    To be called if this
    is running as a cli
    script.
    """
    do_things(prog_name= None)
 
if __name__ == '__main__':
   main()
