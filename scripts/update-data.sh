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

for file in $files; do
    echo "Adding contents of $file..."
    cat "data/$file" >> "$tmp_file"

    if [[ "$file" != $(echo "${files}" | tail -n 1) ]]; then
        echo "" >> "$tmp_file"
    fi
done

mv "$tmp_file" README.md
