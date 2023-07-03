files=$(ls -1 data/ | sort)
tmp_file=$(mktemp)

found_tag=false

while IFS= read -r line; do
    if [[ "$line" == "<!-- data:start -->" ]]; then
        found_tag=true
        echo "$line" >> "$tmp_file"
        continue
    fi

    if $found_tag; then
        continue
    fi

    echo "$line" >> "$tmp_file"
done < README.md

if [[ -f "data/_start.md" ]]; then
    echo "Adding contents of _start.md..."
    cat "data/_start.md" >> "$tmp_file"
fi

for file in $files; do
    if [[ "$file" == _* ]]; then
        continue
    fi

    echo "Adding contents of $file..."
    echo "" >> "$tmp_file"
    echo "<!-- $file -->" >> "$tmp_file"
    cat "data/$file" >> "$tmp_file"
done

if [[ -f "data/_end.md" ]]; then
    echo "Adding contents of _end.md..."
    echo "" >> "$tmp_file"
    cat "data/_end.md" >> "$tmp_file"
fi

mv "$tmp_file" README.md
