"""The expandtabs() method sets the tab size to the specified number of whitespaces. The syntax
is string.expandtabs(tabsize)."""

our_text = 'H\te\tl\tl\to'  # This is our text with tabs in between
print(our_text)  # This will print out initial text

print('-'*30)

tabs_expanded = our_text.expandtabs(2)  # This will chance the tabs to 2 whitespaces
print(tabs_expanded)  # This will print out our new text
